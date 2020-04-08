import {shallowMount} from '@vue/test-utils';
import Pengumuman from '@/components/Pengumuman';

import getAnnouncementDefaultApi from '@/services/pengumumanDataService';

describe('test tabel', () => {
  const wrapper = shallowMount(Pengumuman, {
    'mocks': {
      $session: {
        get: jest.fn().mockReturnValueOnce('admin').mockReturnValueOnce(4),
      },
    },
  });


  it('Tes tabel today', () => {
    expect(wrapper.contains('#table-today')).toBe(true);
  });

  it('Tes table tomorrow', () => {
    expect(wrapper.contains('#table-tomorrow')).toBe(true);
  });

  it('tes detail button', () => {
    getAnnouncementDefaultApi.fetch= jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        pengumuman_tomo: {
          'pk': 0,
          'created_at': '2020-03-01',
          'modified_at': '2020-03-01',
          'tanggal_kelas': '2020-03-02',
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
    expect(wrapper.contains('.detail-button')).toBe(true);
  });
});
