import {shallowMount} from '@vue/test-utils';
import Register from '@/views/Register.vue';
import alumniApi from '@/services/alumniServices';

describe('Tes register page', () => {
  const wrapper = shallowMount(Register, {
    mocks: {
      $refs: {submit: {click: jest.fn()}},
    },
  });

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
    wrapper.vm.clickRegister();
  });

  it('test pre-register - input valid', () => {
    const wrapper = shallowMount(Register, {
      data() {
        return {
          'username': 'luulz',
          'email': 'lulu@gmail.com',
          'password': 'lulusgan',
          'confirm_password': 'lulusgan',
        };
      },
      mocks: {
        $modal: {
          show: jest.fn(),
        },
      },
    });

    wrapper.vm.preRegister();
    expect(wrapper.vm.error).toBe(false);
  });

  alumniApi.registerAlumni = jest.fn((response) => Promise.resolve({
    status: 200,
    data: {
      success: true,
    },
  }));

  it('test pre-register - input kosong', () => {
    const wrapper = shallowMount(Register);

    wrapper.vm.preRegister();
    expect(wrapper.vm.error).toBe(true);
    expect(wrapper.vm.error_message).toBe('Isi semua data terlebih dahulu');
  });

  it('test pre-register - konfirmasi password tidak sesuai', () => {
    const wrapper = shallowMount(Register, {
      data() {
        return {
          'username': 'luulz',
          'email': 'luluaja@ppl.com',
          'password': 'lulusgan',
          'confirm_password': 'semogalulusgan',
        };
      },
    });
    wrapper.vm.preRegister();
    expect(wrapper.vm.error).toBe(true);
    expect(wrapper.vm.error_message).toBe('Konfirmasi password tidak sesuai');
  });
});

describe('Tes konfirmasi password', () => {
  const vm = shallowMount(Register).vm;

  it('Test konfirmasi password sesuai', () => {
    expect(vm.validatePassword('lulusgan', 'galulusgan')).toBe(false);
  });

  it('Test konfirmasi password sesuai', () => {
    expect(vm.validatePassword('lulusgan', 'lulusgan')).toBe(true);
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
      data() {
        return {
          error: false,
          username: 'admin',
          password: 'admin',
          email: 'lulu@gmail.com',
        };
      },
      mocks: {
        $modal: {
          show: jest.fn(),
          hide: jest.fn(),
        },
        $router: {
          push: jest.fn(),
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

  it('test gagal register', () => {
    wrapper.setData({error: true});
    vm.register();
  });

  it('test berhasil register', () => {
    vm.register();
  });

  it('test berhasil processRegister', () => {
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

  it('test error processRegister', () => {
    const error = new Error('error');

    error.response = {
      status: 400,
      data: {
        success: false,
        detail: 'Username sudah terdaftar',
      },
    };
    alumniApi.registerAlumni = jest.fn(() => Promise.reject(error));

    vm.processRegister(request);
    vm.$nextTick(() => {
      expect(vm.modal_message).toBe('Username sudah terdaftar');
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
