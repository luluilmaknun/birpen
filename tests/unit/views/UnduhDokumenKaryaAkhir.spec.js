import {shallowMount} from '@vue/test-utils';
import UnduhDokumenKaryaAkhir from '@/views/UnduhDokumenKaryaAkhir.vue';
import karyaAkhirApi from '@/services/karyaAkhirServices';

describe('Tes konfigurasi dan elemen halaman', () => {
  const wrapper = shallowMount(UnduhDokumenKaryaAkhir);

  it('Kofigurasi vue app name', () => {
    expect(wrapper.name()).toEqual('UnduhDokumenKaryaAkhir');
  });

  it('Elemen halaman', () => {
    expect(wrapper.find('#unduh-semua').exists()).toBe(true);
    expect(wrapper.find('#unduh-semua').html()).toContain('Unduh Semua');
  });
});

describe('Tes fetch data function success', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(UnduhDokumenKaryaAkhir);
    vm = wrapper.vm;

    karyaAkhirApi.fetchDaftarSuratKaryaAkhir = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        surat_karya_akhir:
        [
          {
            'nama': 'Surat Keterangan Karya Akhir Siap Uji',
          },
        ],
      },
    }));

    vm.fetchData();
  });

  it('fetch data success', () => {
    expect(vm.surat_karya_akhir[0].nama)
        .toEqual('Surat Keterangan Karya Akhir Siap Uji');
  });

  it('fetch data success', () => {
    expect(wrapper.findAll('button.unduh-item').length)
        .toBe(1);
  });
});
