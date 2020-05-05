import {shallowMount} from '@vue/test-utils';
import EditStatusSurat from '@/components/edit-status-surat.vue';
import suratAPI from '@/services/suratServices';

const propsData = {
  id_pesanan: '22',
};

describe('tes fetch status surat untuk dropdown', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(EditStatusSurat, {propsData});
    suratAPI.fetchStatusSurat = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        id_pesanan_display: '000001',
        status_surat: [
          {
            pk: 1,
            username: 'Menunggu paraf manager pendidikan',
          },
          {
            pk: 2,
            username: 'Menunggu wakil dekan 1',
          },
          {
            pk: 3,
            username: 'Menunggu wakil dekan',
          },
          {
            pk: 4,
            username: 'Selesai',
          },
        ],
      },
    }));

    vm = wrapper.vm;
    vm.fetchStatusSuratList();
  });

  it('tes fetch status surat', () => {
    expect(vm.list_status_surat.length).toBe(4);
  });
});

describe('tes elemen edit status surat component', () => {
  const wrapper = shallowMount(EditStatusSurat, {propsData});

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

describe('tes update status surat', () => {
  let wrapper; let vm;

  it('success update status surat', () => {
    wrapper = shallowMount(EditStatusSurat, {
      data() {
        return {
          'status_surat_input': 'Selesai',
        };
      },
      propsData,
    });

    suratAPI.updateStatusSurat = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        'success': 'True',
      },
    }));

    vm = wrapper.vm;
    vm.updateStatusSurat();
    expect(vm.status_surat_input).toEqual('Selesai');
  });

  it('fail update surat', () => {
    wrapper = shallowMount(EditStatusSurat, {
      data() {
        return {
          'status_surat_input': 'Kelar',
        };
      },
      propsData,
    });

    suratAPI.updateStatusSurat = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Pesanan surat/jenis dokumen akademik tidak ditemukan.',
      },
    }));

    vm = wrapper.vm;
    vm.updateStatusSurat();
    expect(vm.status_surat_input).toEqual('Kelar');
  });
});
