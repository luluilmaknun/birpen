import {shallowMount} from '@vue/test-utils';
import Pengumuman from '@/views/Pengumuman';

import announcementApi from '@/services/announcementServices';

describe('test tabel exists all', () => {
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
  });

  it('Tes table tomorrow', () => {
    expect(vm.tomorrow.length).toBe(0);
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
      'pembuat': 'asdos',
      'nama_mata_kuliah': 'Struktur Data dan Algoritma',
      'jenis_pengumuman': 'Asistensi',
      'nama_dosen': 'Athallah',
      'nama_asisten': 'Annafis',
      'nama_ruang': '3111',
      'nama_sesi': 'Sesi 4 (17.00 - 19.30)',
      'nama_status_pengumuman': 'Dibatalkan',
      'komentar': 'Corona',
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

  it('tes elemen table today', () => {
    expect(wrapper.find('#nama_dosen_today').text())
        .toBe('Athallah');

    expect(wrapper.find('#nama_mata_kuliah_today').text())
        .toBe('Struktur Data dan Algoritma');

    expect(wrapper.find('#nama_sesi_today').text())
        .toBe('Sesi 4 (17.00 - 19.30)');

    expect(wrapper.find('#nama_status_pengumuman_today').text())
        .toBe('Dibatalkan');
  });

  it('tes elemen table tomorrow', () => {
    expect(wrapper.find('#nama_dosen_tomorrow').text())
        .toBe('Lulu Ilmaknun S.Kom');

    expect(wrapper.find('#nama_mata_kuliah_tomorrow').text())
        .toBe('Analisis Numerik');

    expect(wrapper.find('#nama_sesi_tomorrow').text())
        .toBe('Sesi 2 (11.00 - 13.30)');

    expect(wrapper.find('#nama_status_pengumuman_tomorrow').text())
        .toBe('Terlambat');
  });

  it('Tes tabel today', () => {
    expect(vm.today.length).toBe(1);
  });

  it('Tes table tomorrow', () => {
    expect(vm.tomorrow.length).toBe(1);
  });
});
