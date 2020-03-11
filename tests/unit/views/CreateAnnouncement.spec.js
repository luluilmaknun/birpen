import {shallowMount} from '@vue/test-utils';
import CreateAnnouncement from '@/views/CreateAnnouncement';
import dropdownApi from '@/services/dropdownDataServices';
import announcementApi from '@/services/announcementServices';

describe('Tes Elemen Form', () => {
  const wrapper = shallowMount(CreateAnnouncement);

  it('Buat Pengumuman page name : CreateAnnouncement', () =>{
    expect(wrapper.name()).toEqual('CreateAnnouncement');
  });

  it('punya elemen nama pembuat', () => {
    expect(wrapper.contains('p#pembuat')).toBe(true);
  });

  it('punya elemen tanggal', () => {
    expect(wrapper.contains('input#tanggal_kelas')).toBe(true);
    wrapper.find('input#tanggal_kelas').setValue('2020-03-30');
  });

  it('punya elemen nama mata kuliah', () => {
    expect(wrapper.contains('select#nama_mata_kuliah')).toBe(true);
  });

  it('punya elemen jenis pengumuman', () => {
    expect(wrapper.contains('select#jenis_pengumuman')).toBe(true);
  });

  it('punya elemen nama dosen', () => {
    expect(wrapper.contains('input#nama_dosen')).toBe(true);
  });

  it('punya elemen nama asisten', () => {
    expect(wrapper.contains('input#nama_asisten')).toBe(false);
    wrapper.setData({jenis_pengumuman: 'asistensi'});
  });

  it('punya elemen nama ruang', () => {
    expect(wrapper.contains('select#nama_ruang')).toBe(true);
  });

  it('punya elemen nama sesi', () => {
    expect(wrapper.contains('select#nama_sesi')).toBe(true);
  });

  it('punya elemen nama status pengumuman', () => {
    expect(wrapper.contains('select#nama_status_pengumuman')).toBe(true);
  });

  it('punya elemen komen', () => {
    expect(wrapper.contains('textarea#komentar')).toBe(true);
  });

  it('Tes submit form', () =>{
    wrapper.find('[type=\'submit\']').trigger('click');
  });
});

describe('Tes function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(CreateAnnouncement, {
      'jenis_pengumuman': 'Asistensi',
      'tanggal_kelas': '2020-03-30',
      'nama_mata_kuliah': 'Aljabar Linier',
      'nama_dosen': 'Lulu Ilmaknun',
      'nama_asisten': 'Lulz',
      'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
      'nama_ruang': '3111',
      'nama_status_pengumuman': 'Terlambat',
    });
    vm = wrapper.vm;

    dropdownApi.fetch = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        jenis_pengumuman: ['Asistensi', 'Perkualiahan'],
        mata_kuliah: ['Aljabar Linier', 'Analisis Numerik'],
        ruang: ['3111', '2312'],
        sesi: ['Sesi 1 (08.00 - 10.30)', 'Sesi 2 (11.00 - 13.30)'],
        status_pengumuman: ['Terlambat', 'Dibatalkan'],
      },
    }));

    vm.fetchData();
  });

  it('Test post data', () => {
    wrapper.vm.postData();
  });
});

describe('Edit function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
        pk: 1,
      },
    });
    vm = wrapper.vm;

    announcementApi.getAnnouncement = jest.fn((data) => Promise.resolve({
      status: 200,
      data: {
        pk: 1,
        pembuat: 'lulu',
        nama_mata_kuliah: 'Aljabar Linier',
        jenis_pengumuman: 'Perkuliahan',
        nama_dosen: 'Lulu Ilmaknun',
        tanggal_kelas: '2020-03-30',
        nama_ruang: '3111',
        nama_sesi: 'Sesi 1 (08.00 - 10.30)',
        nama_status_pengumuman: 'Terlambat',
        komentar: 'lol',
      },
    }));

    vm.fetchData();
  });

  it('Test post data', () => {
    vm.postData();
  });

  it('Test edit data', () => {
    expect(wrapper.props('edit')).toBe(true);
    vm.editData(1);
  });
});
