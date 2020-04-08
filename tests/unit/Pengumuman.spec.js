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

  it('Tes get api', () => {
    getAnnouncementDefaultApi.Pengumuman = jest.fn(() => Promise.resolve({
      status: 200,
    }));
  });
});
