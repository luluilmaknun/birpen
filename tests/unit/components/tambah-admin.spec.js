import {shallowMount} from '@vue/test-utils';
import TambahAdmin from '@/components/tambah-admin.vue';
import adminApi from '@/services/adminServices';

describe('Test tambah admin component', () => {
  const wrapper = shallowMount(TambahAdmin);

  it('tes tombol tambah', () => {
    expect(wrapper.find('#tambah').exists()).toBe(true);
    const button = wrapper.find('#tambah');
    button.trigger('click');
  });

  it('tes tombol tambah asisten', () => {
    expect(wrapper.find('#tambah_admin').exists()).toBe(true);
    const button = wrapper.find('#tambah_admin');
    button.trigger('click');
  });
});

describe('tes tambah admin', () => {
  let wrapper; let vm;

  it('success tambah admin', () => {
    wrapper = shallowMount(TambahAdmin, {
      data() {
        return {
          'admin_username': 'athallah',
          'error_message': '',
        };
      },
    });

    adminApi.createAdmin = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        'success': 'True',
      },
    }));

    vm = wrapper.vm;
    vm.click_tambah();
    expect(vm.admin_username).toEqual('athallah');
  });

  it('fail tambah admin, username kosong', () => {
    wrapper = shallowMount(TambahAdmin, {
      data() {
        return {
          'admin_username': '',
          'error_message': 'Username tidak valid',
        };
      },
    });

    adminApi.createAdmin = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Username tidak valid',
      },
    }));

    vm = wrapper.vm;
    vm.click_tambah();
    expect(vm.admin_username).toEqual('');
    expect(vm.error_message).toEqual('Username tidak valid');
  });
});


