import {shallowMount} from '@vue/test-utils';
import Pengumuman from '@/views/Pengumuman';

import getAnnouncementDefaultApi from '@/services/announcementServices';

describe('test tabel', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(Pengumuman);
    vm = wrapper.vm;
    announcementApi.getAnnouncementDefault = jest.fn(
        () => Promise.resolve({
          status: 200,
          data: {
            pengumuman_today: {
              'pk': 0,
              'deleted': null,
              'created_at': '2020-04-08T12:31:04.026691+07:00',
              'modified_at': '2020-04-08T12:31:04.026691+07:00',
              'tanggal_kelas': '2020-04-0',
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
          },
        }));
    vm.fetchData();
  });

  it('tes elemen table', () => {
    expect(wrapper.find('#nama_dosen').element.value)
        .toBe('Lulu Ilmaknun S.Kom');
  });

  it('Tes tabel today', () => {
    expect(vm.today.length).toBe(0);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });

  it('Tes table tomorrow', () => {
    expect(vm.tomorrow.length).toBe(0);
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
    expect(vm.tomorrow.length).toBe(1);
    // VUE GA BISA NGETES V-IF BIND ELEMENT JADI YANG DITES
    // ISI KONDISI DARI VARIABLE CONDITIONNYA AJA
  });
});
