import {shallowMount} from '@vue/test-utils';
import Pengumuman from '@/components/Pengumuman.vue';

describe('Tes Tabel', () => {
  const wrapper = shallowMount(Pengumuman);

  it('apakah tombol detail mengeluarkan modal', () => {
    expect(wrapper.find('.detail-button').exists()).toBe(true);
    const detailButton = wrapper.find('.detail-button');
    detailButton.trigger('click');
  });
});
