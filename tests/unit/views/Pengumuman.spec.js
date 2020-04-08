import {shallowMount} from '@vue/test-utils';
import Pengumuman from '@/views/Pengumuman';

import announcementApi from '@/services/announcementServices';

describe('test tabel not exists all', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(Pengumuman);
    vm = wrapper.vm;
    announcementApi.getAnnouncementDefault = jest.fn(
        (d) => Promise.resolve({
          status: 200,
          data: {
            pengumuman_today: [],
            pengumuman_tomo: [],
          },
        }));
    vm.fetchData();
  });

  it('Tes tabel today', () => {
    expect(vm.today.length).toBe(0);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });

  it('Tes table tomorrow', () => {
    expect(vm.today.length).toBe(0);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });
});

describe('test tabel exists all', () => {
  let wrapper; let vm;

  const pengumumanToday = [
    {
      'pk': 0,
      'deleted': null,
      'created_at': '2020-04-08T12:31:04.026691+07:00',
      'modified_at': '2020-04-08T12:31:04.026691+07:00',
      'tanggal_kelas': '2020-04-30',
      'pembuat': 'dosen',
      'nama_mata_kuliah': 'Analisis Numerik',
      'jenis_pengumuman': 'Perkuliahan',
      'nama_dosen': 'Lulu Ilmaknun S.Kom',
      'nama_asisten': 'Yusuf Tri Ardho',
      'nama_ruang': '2211',
      'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
      'nama_status_pengumuman': 'Terlambat',
      'komentar': 'Saya ada urusan mendadak',
    },
  ];

  const pengumumanTomo = [
    {
      'pk': 0,
      'deleted': null,
      'created_at': '2020-04-08T12:31:04.026691+07:00',
      'modified_at': '2020-04-08T12:31:04.026691+07:00',
      'tanggal_kelas': '2020-04-30',
      'pembuat': 'dosen',
      'nama_mata_kuliah': 'Analisis Numerik',
      'jenis_pengumuman': 'Perkuliahan',
      'nama_dosen': 'Lulu Ilmaknun S.Kom',
      'nama_asisten': 'Yusuf Tri Ardho',
      'nama_ruang': '2211',
      'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
      'nama_status_pengumuman': 'Terlambat',
      'komentar': 'Saya ada urusan mendadak',
    },
  ];

  beforeEach(() => {
    wrapper = shallowMount(Pengumuman);
    vm = wrapper.vm;
    announcementApi.getAnnouncementDefault = jest.fn(
        (d) => Promise.resolve({
          status: 200,
          data: {
            pengumuman_today: pengumumanToday,
            pengumuman_tomo: pengumumanTomo,
          },
        }));
    vm.fetchData();
  });

  it('tes elemen table', () => {
    expect(wrapper.find('#nama_dosen').text())
        .toBe('Lulu Ilmaknun S.Kom');
    // LANJUTIN GAN
  });

  it('Tes tabel today', () => {
    expect(vm.today.length).toBe(1);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });

  it('Tes table tomorrow', () => {
    expect(vm.today.length).toBe(1);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });
});

describe('modal testing', () => {
  let wrapper; let vm;

  const pengumumanToday = [
    {
      'pk': 0,
      'deleted': null,
      'created_at': '2020-04-08T12:31:04.026691+07:00',
      'modified_at': '2020-04-08T12:31:04.026691+07:00',
      'tanggal_kelas': '2020-04-30',
      'pembuat': 'dosen',
      'nama_mata_kuliah': 'Analisis Numerik',
      'jenis_pengumuman': 'Perkuliahan',
      'nama_dosen': 'Lulu Ilmaknun S.Kom',
      'nama_asisten': 'Yusuf Tri Ardho',
      'nama_ruang': '2211',
      'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
      'nama_status_pengumuman': 'Terlambat',
      'komentar': 'Saya ada urusan mendadak',
    },
  ];

  const pengumumanTomo = [
    {
      'pk': 0,
      'deleted': null,
      'created_at': '2020-04-08T12:31:04.026691+07:00',
      'modified_at': '2020-04-08T12:31:04.026691+07:00',
      'tanggal_kelas': '2020-04-30',
      'pembuat': 'dosen',
      'nama_mata_kuliah': 'Analisis Numerik',
      'jenis_pengumuman': 'Perkuliahan',
      'nama_dosen': 'Lulu Ilmaknun S.Kom',
      'nama_asisten': 'Yusuf Tri Ardho',
      'nama_ruang': '2211',
      'nama_sesi': 'Sesi 2 (11.00 - 13.30)',
      'nama_status_pengumuman': 'Terlambat',
      'komentar': 'Saya ada urusan mendadak',
    },
  ];

  beforeEach(() => {
    wrapper = shallowMount(Pengumuman, {
      'mocks': {
        $modal: {
          show: jest.fn(),
          hide: jest.fn(),
        },
      },
    });
    vm = wrapper.vm;

    announcementApi.getAnnouncementDefault = jest.fn(
        (d) => Promise.resolve({
          status: 200,
          data: {
            pengumuman_today: pengumumanToday,
            pengumuman_tomo: pengumumanTomo,
          },
        }));

    vm.fetchData();
  });

  it('tes show modal', () => {
    vm.showModal(
        vm.today[0]['pk'],
        vm.today[0]['pembuat'],
        vm.today[0]['created_at'],
        vm.today[0]['nama_mata_kuliah'],
        vm.today[0]['jenis_pengumuman'],
        vm.today[0]['nama_dosen'],
        vm.today[0]['nama_asisten'],
        vm.today[0]['nama_ruang'],
        vm.today[0]['nama_sesi'],
        vm.today[0]['nama_status_pengumuman'],
        vm.today[0]['komentar'],
    );

    expect(vm.$modal.show).toHaveBeenCalledWith('detail-modal');
  });

  it('tes close modal', () => {
    vm.closeModal();

    expect(vm.$modal.hide).toHaveBeenCalledWith('detail-modal');
  });
});
