import {shallowMount} from '@vue/test-utils';
import DetailPengajuanSurat from '@/views/DetailPengajuanSurat.vue';

describe('Test fetch', () => {
  let wrapper;
  let vm;

  const mockResponse = {
    'nama_pemesan': 'Ardo',
    'npm_pemesan': '1706075200',
    'pesanan_surat_akademik': [
      {
        'jumlah': 4,
        'status_surat': 'Bisa Diambil',
        'surat_akademik': 'Cetak/Denda: FRS/IRS',
      },
    ],
    'pk': '12',
    'status_bayar': 'Belum Bayar',
    'waktu_pemesanan': '2020-05-06T06:39:12.00+07:00',
  };

  const paddingPK = String(mockResponse.pk).padStart(6, '0');
  it('test fetch', () => {
    wrapper = shallowMount(DetailPengajuanSurat, {
      data() {
        return {
          detailPesanan: mockResponse,
        };
      },
    });
    vm = wrapper.vm;
    vm.fetchDetail(paddingPK);
  });
});
