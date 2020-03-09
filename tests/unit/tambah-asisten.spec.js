import {shallowMount} from '@vue/test-utils';
import TambahAsisten from '@/components/tambah-asisten.vue';

describe('Test tambah asisten component', () => {
  const wrapper = shallowMount(TambahAsisten);

  it('tes tombol tambah', () => {
    expect(wrapper.find('#tambah').exists()).toBe(true);
    const detailButton = wrapper.find('#tambah');
    detailButton.trigger('click');
  });

  it('tes tombol tambah asisten', () => {
    expect(wrapper.find('#tambah_asisten').exists()).toBe(true);
    const detailButton = wrapper.find('#tambah_asisten');
    detailButton.trigger('click');
  });
});
