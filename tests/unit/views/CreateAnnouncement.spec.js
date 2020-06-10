import {shallowMount} from '@vue/test-utils';
import CreateAnnouncement from '@/views/CreateAnnouncement';
import dropdownApi from '@/services/dropdownDataServices';
import announcementApi from '@/services/announcementServices';

describe('Tes Elemen Form', () => {
  const wrapper = shallowMount(CreateAnnouncement);
  wrapper.setData({
    isFetchData: false,
    isGetAnnouncementData: false,
  });

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

describe('Tes create data function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(CreateAnnouncement, {
      data() {
        return {
          'jenis_pengumuman': 'Asistensi',
          'tanggal_kelas': '2100-03-30',
          'nama_mata_kuliah': 'Aljabar Linier',
          'nama_dosen': 'Lulu Ilmaknun',
          'nama_asisten': 'Lulz',
          'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
          'nama_ruang': '3111',
          'nama_status_pengumuman': 'Terlambat',
        };
      },
    });
    vm = wrapper.vm;

    dropdownApi.fetch = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        jenis_pengumuman: ['Asistensi', 'Perkuliahan'],
        mata_kuliah: ['Aljabar Linier', 'Analisis Numerik', 'Basdut'],
        ruang: ['3111'],
        sesi: ['Sesi 1 (08.00 - 10.30)', 'Sesi 2 (11.00 - 13.30)'],
        status_pengumuman: ['Terlambat', 'Dibatalkan', 'Dihancurkan'],
      },
    }));

    vm.fetchData();
  });

  it('Test fetched data', () => {
    expect(wrapper.find('#jenis_pengumuman').findAll('option').length)
        .toBe(2);
    expect(wrapper.find('#nama_mata_kuliah').findAll('option').length)
        .toBe(3);
    expect(wrapper.find('#nama_ruang').findAll('option').length)
        .toBe(1);
    expect(wrapper.find('#nama_sesi').findAll('option').length)
        .toBe(2);
    expect(wrapper.find('#nama_status_pengumuman').findAll('option').length)
        .toBe(3);
  });

  it('Test data return', () => {
    expect(wrapper.find('#nama_dosen').element.value)
        .toBe('Lulu Ilmaknun');
    expect(wrapper.find('#tanggal_kelas').element.value)
        .toBe('2100-03-30');
    expect(wrapper.find('#jenis_pengumuman').element.value)
        .toBe('Asistensi');
    expect(wrapper.find('#nama_asisten').element.value)
        .toBe('Lulz');
    expect(wrapper.find('#nama_mata_kuliah').element.value)
        .toBe('Aljabar Linier');
    expect(wrapper.find('#nama_sesi').element.value)
        .toBe('Sesi 2 (11.00 - 13.30)');
    expect(wrapper.find('#nama_ruang').element.value)
        .toBe('3111');
    expect(wrapper.find('#nama_status_pengumuman').element.value)
        .toBe('Terlambat');
  });

  it('Test create data success', () => {
    announcementApi.createAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        detail: 'Valid data.',
        success: true,
      },
    }));

    vm.validateData();
  });

  it('Test create data error', () => {
    const wrapper = shallowMount(CreateAnnouncement, {
      data() {
        return {
          'jenis_pengumuman': 'Asistensi',
          'tanggal_kelas': '2001-03-30',
          'nama_mata_kuliah': 'Aljabar Linier',
          'nama_dosen': 'Lulu Ilmaknun',
          'nama_asisten': 'Lulz',
          'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
          'nama_ruang': '3111',
          'nama_status_pengumuman': 'Terlambat',
        };
      },
    });
    const vm = wrapper.vm;

    vm.validateData();
    expect(wrapper.vm.error_message_seen).toBe(true);
    expect(wrapper.vm.error_message).toBe('Kelas sudah lampau');
  });

  it('Test create data error from backend', () => {
    const error = new Error('error');

    error.response = {
      status: 400,
      data: {
        success: false,
        detail: 'Tidak punya wewenang untuk membuat',
      },
    };

    announcementApi.createAnnouncement = jest.fn(() =>
      Promise.reject(error));

    vm.validateData();
    vm.$nextTick(() => {
      expect(wrapper.vm.error_message_seen).toBe(true);
      expect(wrapper.vm.error_message)
          .toBe('Tidak punya wewenang untuk membuat');
    });
  });
});

describe('Edit function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
    });
    vm = wrapper.vm;

    announcementApi.getAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman: {
          'pk': '1',
          'pembuat': 'lulu',
          'nama_mata_kuliah': 'Aljabar Linier',
          'jenis_pengumuman': 'Asistensi',
          'nama_asisten': 'Lulu ajah',
          'nama_dosen': 'Lulu Ilmaknun',
          'tanggal_kelas': '2200-03-30',
          'nama_ruang': '3111',
          'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
          'nama_status_pengumuman': 'Terlambat',
          'komentar': 'lol',
        },
      },
    }));

    announcementApi.editAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        detail: 'Valid data.',
        success: true,
      },
    }));

    vm.getAnnouncementData(1);
  });

  it('Test data return', () => {
    expect(wrapper.find('#nama_dosen').element.value)
        .toBe('Lulu Ilmaknun');
    expect(wrapper.find('#tanggal_kelas').element.value)
        .toBe('2200-03-30');
    expect(wrapper.find('#nama_mata_kuliah').element.value)
        .toBe('Aljabar Linier');
    expect(wrapper.find('#nama_sesi').element.value)
        .toBe('Sesi 1 (08.00 - 10.30)');
    expect(wrapper.find('#jenis_pengumuman').element.value)
        .toBe('Asistensi');
    expect(wrapper.find('#nama_asisten').element.value)
        .toBe('Lulu ajah');
    expect(wrapper.find('#nama_ruang').element.value)
        .toBe('3111');
    expect(wrapper.find('#nama_status_pengumuman').element.value)
        .toBe('Terlambat');
    expect(wrapper.find('#komentar').element.value)
        .toBe('lol');
  });

  it('Test edit data success', () => {
    expect(wrapper.props('edit')).toBe(true);
    const namaDosen = wrapper.find('#nama_dosen');
    namaDosen.element.value = 'Bukan Lulu';
    namaDosen.trigger('change');

    vm.validateData();
    vm.getAnnouncementData(1);

    expect(wrapper.find('#nama_dosen').element.value)
        .toBe('Bukan Lulu');
  });

  it('Test edit data error', () => {
    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
      data() {
        return {
          'jenis_pengumuman': 'Asistensi',
          'tanggal_kelas': '2001-03-30',
          'nama_mata_kuliah': 'Aljabar Linier',
          'nama_dosen': 'Lulu Ilmaknun',
          'nama_asisten': 'Lulz',
          'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
          'nama_ruang': '3111',
          'nama_status_pengumuman': 'Terlambat',
        };
      },
    });
    const vm = wrapper.vm;

    vm.validateData();
    expect(wrapper.vm.error_message_seen).toBe(true);
    expect(wrapper.vm.error_message).toBe('Kelas sudah lampau');
  });

  it('Test security access admin success', () => {
    announcementApi.getAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman: {
          'pk': '1',
          'pembuat': 'lulu',
          'nama_mata_kuliah': 'Aljabar Linier',
          'jenis_pengumuman': 'Asistensi',
          'nama_asisten': 'Lulu ajah',
          'nama_dosen': 'Lulu Ilmaknun',
          'tanggal_kelas': '2200-03-30',
          'nama_ruang': '3111',
          'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
          'nama_status_pengumuman': 'Terlambat',
          'komentar': 'lol',
        },
      },
    }));

    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
    });
    const vm = wrapper.vm;

    vm.getAnnouncementData(1);
  });

  it('Test security access non-admin success asistensi', () => {
    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
    });
    const vm = wrapper.vm;

    announcementApi.getAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman: {
          'pk': '1',
          'pembuat': 'lulu.ilmaknun',
          'nama_mata_kuliah': 'Aljabar Linier',
          'jenis_pengumuman': 'Asistensi',
          'nama_asisten': 'Lulu ajah',
          'nama_dosen': 'Lulu Ilmaknun',
          'tanggal_kelas': '2200-03-30',
          'nama_ruang': '3111',
          'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
          'nama_status_pengumuman': 'Terlambat',
          'komentar': 'lol',
        },
      },
    }));

    vm.getAnnouncementData(1);
  });

  it('Test security access non-admin success non-asistensi', () => {
    const localStorageMock = {
      data: {
        username: 'lulu.ilmaknun',
        role: 'mahasiswa',
        is_admin: 'false',
        is_asdos: 'false',
      },
      length: 4,
      getItem(name) {
        return this.data[name];
      },
    };

    Object.defineProperty(window, 'localStorage', {
      value: localStorageMock,
    });

    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
    });
    const vm = wrapper.vm;

    announcementApi.getAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman: {
          'pk': '1',
          'pembuat': 'lulu.ilmaknun',
          'nama_mata_kuliah': 'Aljabar Linier',
          'jenis_pengumuman': 'Perkuliahan',
          'nama_dosen': 'Lulu Ilmaknun',
          'tanggal_kelas': '2200-03-30',
          'nama_ruang': '3111',
          'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
          'nama_status_pengumuman': 'Terlambat',
          'komentar': 'lol',
        },
      },
    }));

    vm.getAnnouncementData(1);
  });

  it('Test security access non-admin denied asistensi', () => {
    const localStorageMock = {
      data: {
        username: 'lulu.ilmaknun',
        role: 'mahasiswa',
        is_admin: 'false',
        is_asdos: 'false',
      },
      length: 4,
      getItem(name) {
        return this.data[name];
      },
    };

    Object.defineProperty(window, 'localStorage', {
      value: localStorageMock,
    });

    announcementApi.getAnnouncement = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman: {
          'pk': '1',
          'pembuat': 'lulu',
          'nama_mata_kuliah': 'Aljabar Linier',
          'jenis_pengumuman': 'Asistensi',
          'nama_asisten': 'Lulu ajah',
          'nama_dosen': 'Lulu Ilmaknun',
          'tanggal_kelas': '2200-03-30',
          'nama_ruang': '3111',
          'nama_sesi': 'Sesi 1 (08.00 - 10.30)',
          'nama_status_pengumuman': 'Terlambat',
          'komentar': 'lol',
        },
      },
    }));

    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
      'mocks': {
        $router: {
          push: jest.fn(),
        },
      },
    });
    const vm = wrapper.vm;

    vm.getAnnouncementData();
  });

  it('Test edit data error from backend', () => {
    const wrapper = shallowMount(CreateAnnouncement, {
      'propsData': {
        edit: true,
      },
      data() {
        return {
          'jenis_pengumuman': 'Asistensi',
          'tanggal_kelas': '2200-03-30',
          'nama_mata_kuliah': 'Aljabar Linier',
          'nama_dosen': 'Lulu Ilmaknun',
          'nama_asisten': 'Lulz',
          'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
          'nama_ruang': '3111',
          'nama_status_pengumuman': 'Terlambat',
        };
      },
    });
    const vm = wrapper.vm;

    const error = new Error('error');
    error.response = {
      status: 400,
      data: {
        success: false,
        detail: 'Tidak punya wewenang untuk mengubah',
      },
    };

    announcementApi.editAnnouncement = jest.fn(() =>
      Promise.reject(error));

    vm.validateData();
    vm.$nextTick(() => {
      expect(wrapper.vm.error_message)
          .toBe('Tidak punya wewenang untuk mengubah');
      expect(wrapper.vm.error_message_seen).toBe(true);
    });
  });
});
