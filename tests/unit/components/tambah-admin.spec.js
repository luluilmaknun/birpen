import {shallowMount} from '@vue/test-utils';
import TambahAdmin from '@/components/tambah-admin.vue';
// import adminApi from '@/services/adminServices';

describe('Test tambah admin component', () => {
  const wrapper = shallowMount(TambahAdmin);

  it('tes tombol tambah admin', () => {
    expect(wrapper.find('#tambah').exists()).toBe(true);
    const button = wrapper.find('#tambah');
    button.trigger('click');
  });

  it('tes tambah asisten', () => {
    expect(wrapper.find('#tambah_admin').exists()).toBe(true);
    const button = wrapper.find('#tambah_admin');
    button.trigger('click');
  });
});

