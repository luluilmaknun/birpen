import {shallowMount, createLocalVue} from '@vue/test-utils';
import Navigation from '@/components/Navigation.vue';

describe('Tes base navbar', () => {
  const wrapper = shallowMount(Navigation);

  it('apakah base navbar ada tombol Buat akun', () => {
    const button = wrapper.find({ref: 'buatAkun-button'});
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Buat Akun');
  });

  it('apakah base navbar ada tombol Login', () => {
    const button = wrapper.find({ref: 'login'});
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Login');
  });

  it('apakah base navbar ada tombol Pengumuman', () => {
    const button = wrapper.find({ref: 'pengumuman-button'});
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Pengumuman');
  });

  it('apakah base navbar ada tombol Surat', () => {
    const button = wrapper.find({ref: 'surat-button'});
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Surat');
  });

  it('test user telah login', () => {
    const localVue = createLocalVue();
    localStorage.setItem('token', '5e8u4Ht0k3n');

    const wrapper = shallowMount(Navigation, {
      localVue,
    });

    const vm = wrapper.vm;
    expect(vm.is_authenticated).toBe(true);
    localStorage.clear();
  });

  it('test user belum login', () => {
    const localVue = createLocalVue();

    const wrapper = shallowMount(Navigation, {
      localVue,
    });

    const vm = wrapper.vm;
    expect(vm.is_authenticated).toBe(false);
  });
});
