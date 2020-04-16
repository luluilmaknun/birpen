import {shallowMount} from '@vue/test-utils';
import DeleteAdmin from '@/components/delete-admin.vue';
import adminApi from '@/services/adminServices';

describe('Test hapus component', () => {
  const wrapper = shallowMount(DeleteAdmin);

  it('tes tombol hapus', () => {
    expect(wrapper.find('#remove-btn').exists()).toBe(true);
    const button = wrapper.find('#remove-btn');
    button.trigger('click');
  });

  it('tes tombol konfirmasi -> tidak', () => {
    expect(wrapper.find('#tidak').exists()).toBe(true);
    const button = wrapper.find('#tidak');
    button.trigger('click');
  });

  it('tes tombol konfirmasi -> hapus', () => {
    expect(wrapper.find('#hapus_conf').exists()).toBe(true);
    const button = wrapper.find('#hapus_conf');
    button.trigger('click');
  });
});

describe('tes hapus admin', () => {
  let wrapper; let vm;

  it('success hapus admin', () => {
    wrapper = shallowMount(DeleteAdmin, {
      data() {
        return {
          'deleted_admin_username': 'admiranda',
        };
      },
    });

    adminApi.deleteAdmin = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        'success': 'True',
      },
    }));

    vm = wrapper.vm;
    vm.click_hapus_conf();
  });

  it('fail hapus admin, admin tidak ada', () => {
    wrapper = shallowMount(DeleteAdmin, {
      data() {
        return {
          'deleted_admin_username': 's4y@_bkN_4dm1n',
        };
      },
    });

    adminApi.createAdmin = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Admin does not exist.',
      },
    }));

    vm = wrapper.vm;
    vm.click_hapus_conf();
  });
});
