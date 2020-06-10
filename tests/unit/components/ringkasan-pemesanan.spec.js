import {shallowMount} from '@vue/test-utils';
import RingkasanPemesanan from '@/components/ringkasan-pemesanan';

describe('Tes Elemen', () => {
  const wrapper = shallowMount(RingkasanPemesanan);

  it('Ringkasan Pemesanan page name', () => {
    expect(wrapper.name()).toEqual('RingkasanPemesanan');
  });

  it('Attribute', () => {
    const tableHead = ['Jenis Dokumen', 'Harga', 'Jumlah'];
    expect(wrapper.vm.tableHead).toEqual(tableHead);
  });
});
