import {shallowMount, createLocalVue} from '@vue/test-utils';
import VueModal from 'vue-js-modal';
import DetailKaryaAkhir from '@/components/detail-karya-akhir';
import karyaAkhirAPI from '@/services/karyaAkhirServices';


const localVue = createLocalVue();
localVue.use(VueModal);

const propsData = {
  username: 'yusuf.tri71',
};

describe('tes detail karya akhir komponen', () => {
  const wrapper = shallowMount(DetailKaryaAkhir, {
    propsData, localVue,
  });

  it('tes tombol buka modal (detail)', () => {
    const button = wrapper.find('.detail-btn');
    expect(button.exists()).toBe(true);
    button.trigger('click');
  });

  it('tes tombol tutup modal', () => {
    const button = wrapper.find('.close-btn');
    expect(button.exists()).toBe(true);
    button.trigger('click');
  });

  it('tes loader', () => {
    expect(wrapper.find('.loader-container').exists());
  });
});

describe('tes fetch detail', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(DetailKaryaAkhir, {
      propsData, localVue,
    });
    vm = wrapper.vm;

    karyaAkhirAPI.fetchDetail = jest.fn(() => Promise.resolve({
      data: {
        data_karya_akhir: {
          mahasiswa: {
            nama: 'Yusuf Tri Ardho',
            npm: '1706074985',
            program_studi: 'Ilmu Komputer',
            peminatan_mahasiswa: 'SE',
          },
          jenis_karya_akhir: 'Skripsi',
          sks_diperoleh: '144',
          pembimbing: 'lulu',
          pembimbing_pendamping: 'nafis',
          judul_karya_id: 'kucing',
          judul_karya_en: 'cat',
          isLoadDetail: 'false',
        },
      },
    }));
  });

  it('tes fetch detail', () => {
    vm.fetchDetail();
  });
});
