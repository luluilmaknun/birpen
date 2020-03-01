import {mount} from '@vue/test-utils';
import Navbase from '../../src/components/Navigation.vue';

describe('Tes base navbar', () => {
  const wrapper = mount(Navbase);
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

    it('button Surat redirect', () => {
      const button = wrapper.find({ref: 'surat-button'});
      window.location.assign = jest.fn();
      button.trigger('click');
      expect(window.location.assign).toHaveBeenCalledWith('/surat');
    });

    it('button Pengumuman redirect', () => {
      const button = wrapper.find({ref: 'pengumuman-button'});
      window.location.assign = jest.fn();
      button.trigger('click');
      expect(window.location.assign).toHaveBeenCalledWith('/pengumuman');
    });


    it('button Login redirect', () => {
      const button = wrapper.find({ref: 'login'});
      window.location.assign = jest.fn();
      button.trigger('click');
      expect(window.location.assign).toHaveBeenCalledWith('/login');
    });

  it('button buat akun redirect', () => {
    const button = wrapper.find({ref: 'buat-akun'});
    window.location.assign = jest.fn();
    button.trigger('click');
    expect(window.location.assign).toHaveBeenCalledWith('/buatAkun');
  });
});
