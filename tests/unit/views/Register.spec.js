import {shallowMount} from '@vue/test-utils';
import Register from '@/views/Register.vue';
import alumniApi from '@/services/alumniServices';

describe('Tes register page', () => {
  const wrapper = shallowMount(Register);

  it('apakah ada field username', () => {
    const field = wrapper.find('.username-input');
    expect(field.exists()).toBe(true);
    expect(wrapper.html()).toContain('Username:');
  });

  it('apakah ada field email', () => {
    const field = wrapper.find('.email-input');
    expect(field.exists()).toBe(true);
    expect(wrapper.html()).toContain('Email:');
  });

  it('apakah ada field password', () => {
    const field = wrapper.find('.password-input');
    expect(field.exists()).toBe(true);
    expect(wrapper.html()).toContain('Password:');
  });

  it('apakah tombol daftar bisa diklik', () => {
    const button = wrapper.find('.register-button');
    expect(button.exists()).toBe(true);
    expect(button.html()).toContain('DAFTAR');
    button.trigger('click');
  });

  it('test klik enter', () => {
    wrapper.find('#username').trigger('keyup.enter');
    wrapper.find('#password').trigger('keyup.enter');
    wrapper.find('#email').trigger('keyup.enter');
  });

  it('test klik enter untuk masuk - input valid', () => {
    const wrapper = shallowMount(Register, {
      data() {
        return {
          'username': 'luulz',
          'email': 'lulu@gmail.com',
          'password': 'lulusgan',
        };
      },
    });
    wrapper.find('#email').trigger('keyup.enter');
  });

  alumniApi.registerAlumni = jest.fn((response) => Promise.resolve({
    status: 200,
    data: {
      success: true,
    },
  }));

  it('test klik enter untuk masuk - input kosong', () => {
    const wrapper = shallowMount(Register);

    wrapper.vm.register();
    expect(wrapper.vm.message_seen).toBe(true);
    expect(wrapper.vm.error_message).toBe('Isi semua data terlebih dahulu');
  });

  it('test klik enter untuk masuk - email tidak valid', () => {
    const wrapper = shallowMount(Register, {
      data() {
        return {
          'username': 'luulz',
          'email': 'luluaja',
          'password': 'lulusgan',
        };
      },
    });

    wrapper.vm.register();
    expect(wrapper.vm.message_seen).toBe(true);
    expect(wrapper.vm.error_message)
        .toBe('Masukkan alamat email yang valid');
  });
});

describe('Tes validasi email', () => {
  const vm = shallowMount(Register).vm;

  it('Tes sukses', () => {
    expect(vm.validateEmail('lulu@lulu.com'))
        .toBe(true);
  });

  it('Tes gagal', () => {
    expect(vm.validateEmail('lulululu.com'))
        .toBe(false);
  });
});

describe('Tes modal', () => {
  const vm = shallowMount(Register, {
    'mocks': {
      $modal: {
        hide: jest.fn(),
        show: jest.fn(),
      },
    },
  }).vm;

  it('Tes close Modal', () => {
    vm.closeModal();
  });

  it('Tes show Modal', () => {
    vm.showModal();
  });
});

describe('Tes register', () => {
  let wrapper; let vm; let request;

  beforeEach(() => {
    wrapper = shallowMount(Register, {
      mocks: {
        $modal: {
          show: jest.fn(),
        },
      },
    });
    vm = wrapper.vm;

    request = {
      'username': 'admin',
      'password': 'admin',
      'email': 'lulu@gmail.com',
    };
  });

  it('test berhasil', () => {
    alumniApi.registerAlumni = jest.fn((_) => Promise.resolve({
      status: 200,
      data: {
        success: true,
      },
    }));

    vm.processRegister(request);
    vm.$nextTick(() => {
      expect(vm.modal_message).toBe('Berhasil membuat akun');
    });
  });

  it('test error', () => {
    const error = new Error('error');

    error.response = {
      status: 400,
      data: {
        success: false,
        detail: 'Username is already exist.',
      },
    };
    alumniApi.registerAlumni = jest.fn(() => Promise.reject(error));

    vm.processRegister(request);
    vm.$nextTick(() => {
      expect(vm.modal_message).toBe('Username is already exist.');
    });
  });

  it('goToPage() method', () => {
    const wrapper = shallowMount(Register, {
      'mocks': {
        $router: {
          push: jest.fn(),
        },
      },
    });

    wrapper.vm.goToPage('login');
  });
});
