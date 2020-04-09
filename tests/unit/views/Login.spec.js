import {shallowMount, createLocalVue} from '@vue/test-utils';
import Login from '@/views/Login.vue';
import VueRouter from 'vue-router';

const localVue = createLocalVue();
localVue.use(VueRouter);
const router = new VueRouter();

jest.mock('axios', () => {
  return {
    post: jest.fn(() => Promise.resolve({data: {}})),
  };
});

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

describe('Tes login non sso', () => {
  const wrapper = shallowMount(Login, {
    localVue,
    router,
    data() {
      return {
        username: 'admin',
        password: 'admin',
      };
    },
    mocks: {
      $router: {
        push: jest.fn(),
      },
    },
  });

  const vm = wrapper.vm;

  it('test berhasil', () => {
    vm.login();
  });
});
