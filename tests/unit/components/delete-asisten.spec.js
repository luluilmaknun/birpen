import {shallowMount} from '@vue/test-utils';
import DeleteAsisten from '@/components/delete-asisten.vue';
import asistenApi from '@/services/asistenServices';

describe('Test hapus component', () => {
  const wrapper = shallowMount(DeleteAsisten);

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

describe('tes hapus asisten', () => {
  let wrapper; let vm;

  it('success hapus asisten', () => {
    wrapper = shallowMount(DeleteAsisten, {
      data() {
        return {
          'deleted_asisten_username': 'admiranda',
          'error_message': '',
        };
      },
    });

    asistenApi.deleteAsisten = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        'success': 'True',
      },
    }));

    vm = wrapper.vm;
    vm.click_hapus_conf();
  });

  it('fail hapus asisten, asisten tidak ada', () => {
    wrapper = shallowMount(DeleteAsisten, {
      data() {
        return {
          'deleted_asisten_username': 's4y@_bkN_451sTen',
          'error_message': 'Admin does not exist.',
        };
      },
    });

    asistenApi.createasisten = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Asisten does not exist.',
      },
    }));

    vm = wrapper.vm;
    vm.click_hapus_conf();
    expect(vm.error_message).toEqual('Admin does not exist.');
  });
});
