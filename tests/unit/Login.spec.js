import {shallowMount} from '@vue/test-utils';
import Login from '@/components/Login.vue';

describe('Tes login page', () => {
  const wrapper = shallowMount(Login);

  it('apakah ada field username', () => {
    const field = wrapper.find('.username-input');
    expect(field.exists()).toBe(true);
    expect(wrapper.html()).toContain('Username:');
  });

  it('apakah ada field password', () => {
    const field = wrapper.find('.password-input');
    expect(field.exists()).toBe(true);
    expect(wrapper.html()).toContain('Password:');
  });

  it('apakah tombol masuk bisa diklik', () => {
    const button = wrapper.find('.login-button');
    expect(button.exists()).toBe(true);
    button.trigger('click');
  });

  it('apakah terdapat tombol buat akun', () => {
    const button = wrapper.find('#buat-akun');
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Buat Akun');
  });

  it('apakah terdapat tombol login dengan SSO', () => {
    const button = wrapper.find('#sso-link');
    expect(button.exists()).toBe(true);
    expect(wrapper.html()).toContain('Login with<br>SSO');
  });
});
