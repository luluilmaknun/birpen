import {shallowMount, createLocalVue} from '@vue/test-utils';
import Navigation from '@/App.vue';
import axios from 'axios';
import sinon from 'sinon';
import VueRouter from 'vue-router';

const localVue = createLocalVue();
localVue.use(VueRouter);
const router = new VueRouter();

jest.mock('axios', () => {
  return {
    get: jest.fn(() => Promise.resolve({data: {}})),
  };
});

describe('Tes Halaman Utama', () => {
  const wrapper = shallowMount(Navigation, {
    localVue,
    router,
  });
  it('App name : Navigation', () =>{
    expect(wrapper.name()).toEqual(undefined);
  });
});

describe('Test Refresh Token', () => {
  sinon.stub(window.location, 'replace');

  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Navigation, {
      localVue,
      router,
      stubs: ['router-link', 'router-view'],
    });
    localStorage.setItem('token', 'Abwaba');
  });

  afterEach(() => {
    jest.clearAllMocks();
    wrapper.destroy();
  });

  const mockResponseDataSuccess = jest.fn(() => {
    return {
      status: 200,
      data: {
        token: 'VBfaXaAslFFaazaAA',
        username: 'username',
        role: 'mahasiswa',
        is_admin: false,
        is_asdos: false,
      },
    };
  });

  const mockResponseDataFail = jest.fn(() => {
    return {
      status: 400,
      data: {
        detail: 'Error decoding token.',
      },
    };
  });

  it('Test refresh token success', async () => {
    jest.spyOn(window.localStorage.__proto__, 'setItem');
    window.localStorage.__proto__.setItem = jest.fn();

    const data = mockResponseDataSuccess();

    axios.get.mockImplementationOnce(() => {
      return Promise.resolve(data);
    });

    await expect(wrapper.vm.refreshData()).resolves.toBe(undefined);
    expect(localStorage.setItem).toHaveBeenCalled();
  });

  it('Test refresh token get error status', async () => {
    jest.spyOn(window.localStorage.__proto__, 'setItem');
    window.localStorage.__proto__.clear = jest.fn();

    const data = mockResponseDataFail();

    axios.get.mockRejectedValueOnce(() => {
      return Promise.reject(data);
    });

    await expect(wrapper.vm.refreshData()).resolves.toBe(undefined);
    expect(localStorage.clear).toHaveBeenCalled();
  });
});

describe('Test watch route', () => {
  it('Should called on route change', function(end) {
    jest.spyOn(window.localStorage.__proto__, 'setItem');
    window.localStorage.__proto__.setItem = jest.fn();

    const wrapper = shallowMount(Navigation, {
      localVue,
      router,
      stubs: ['router-link', 'router-view'],
    });

    wrapper.vm.$router.push('/pengumuman');
    setTimeout(() => {
      expect(localStorage.setItem).toHaveBeenCalled();
      end();
    }, 0);
  });
});
