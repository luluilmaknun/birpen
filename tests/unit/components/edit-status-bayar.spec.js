import {shallowMount} from '@vue/test-utils';
import EditStatusBayar from '@/components/edit-status-bayar.vue';
import suratAPI from '@/services/suratServices';

const propsData = {
  id_pesanan: '32',
};

describe('tes fetch status bayar untuk dropdown', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(EditStatusBayar, {propsData});
    suratAPI.fetchStatusBayar = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        id_pesanan_display: '000001',
        status_bayar: [
          {
            pk: 1,
            username: 'Belum bayar',
          },
          {
            pk: 2,
            username: 'Lunas',
          },
        ],
      },
    }));

    vm = wrapper.vm;
    vm.fetchStatusBayarList();
  });

  it('tes fetch status bayar', () => {
    expect(vm.list_status_bayar.length).toBe(2);
  });
});

describe('tes elemen edit status bayar component', () => {
  const wrapper = shallowMount(EditStatusBayar, {propsData});

  it('tes edit button', () => {
    expect(wrapper.find('#pen-icon').exists()).toBe(true);
    const button = wrapper.find('#pen-icon');
    button.trigger('click');
  });

  it('tes simpan button', () => {
    expect(wrapper.find('#simpan-button').exists()).toBe(true);
    const button = wrapper.find('#simpan-button');
    button.trigger('click');
  });
});

describe('tes update status bayar', () => {
  let wrapper; let vm;

  it('success update status bayar', () => {
    wrapper = shallowMount(EditStatusBayar, {
      data() {
        return {
          'status_bayar_input': 'Lunas',
        };
      },
      propsData,
    });

    suratAPI.updateStatusBayar = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        'success': 'True',
      },
    }));

    vm = wrapper.vm;
    vm.updateStatusBayar();
    expect(vm.status_bayar_input).toEqual('Lunas');
  });

  it('fail update status bayar', () => {
    wrapper = shallowMount(EditStatusBayar, {
      data() {
        return {
          'status_bayar_input': 'Ngutang',
        };
      },
      propsData,
    });

    suratAPI.updateStatusBayar = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Pesanan surat/jenis status bayar tidak ditemukan.',
      },
    }));

    vm = wrapper.vm;
    vm.updateStatusBayar();
    expect(vm.status_bayar_input).toEqual('Ngutang');
  });
});
