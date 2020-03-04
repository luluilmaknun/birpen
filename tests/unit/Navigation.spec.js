import {shallowMount} from '@vue/test-utils';
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
});
