import {shallowMount} from '@vue/test-utils';
import TambahAsisten from '@/components/tambah-asisten.vue';
import asistenApi from '@/services/asistenServices';

describe('Test tambah asisten component', () => {
  const wrapper = shallowMount(TambahAsisten);

  it('tes tombol tambah asisten', () => {
    expect(wrapper.find('#tambah').exists()).toBe(true);
    const detailButton = wrapper.find('#tambah');
    detailButton.trigger('click');
  });

  it('tes tambah asisten', () => {
    expect(wrapper.find('#tambah_asisten').exists()).toBe(true);
    const detailButton = wrapper.find('#tambah_asisten');
    detailButton.trigger('click');
  });
});

describe('tes tambah asisten', () => {
  let wrapper; let vm;

  it('success add asisten', () => {
    wrapper = shallowMount(TambahAsisten, {
      data() {
        return {
          'sso_username': 'yusuf.tri71',
          'error_message': '',
        };
      },
    });

    asistenApi.createAsisten = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        detail: 'Valid data.',
        success: 'True',
      },
    }));

    vm = wrapper.vm;
    vm.click_tambah();
    expect(vm.sso_username).toEqual('yusuf.tri71');
  });

  it('fail add asisten', () => {
    wrapper = shallowMount(TambahAsisten, {
      data() {
        return {
          'sso_username': '',
          'error_message': 'Username tidak valid',
        };
      },
    });

    asistenApi.createAsisten = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Username tidak valid',
        success: 'False',
      },
    }));

    vm = wrapper.vm;
    vm.click_tambah();
    expect(vm.sso_username).toEqual('');
    expect(vm.error_message).toEqual('Username tidak valid');
  });
});
