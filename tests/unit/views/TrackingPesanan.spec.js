import {shallowMount} from '@vue/test-utils';
import TrackingPesanan from '@/views/TrackingPesanan.vue';

describe('Cek komponen tabel', () => {
  const wrapper = shallowMount(TrackingPesanan);

  it('Tes kolom pk', () => {
    expect(wrapper.find('#pk').exists()).toBe(true);
  });

  it('Tes kolom nama pemesan', () => {
    expect(wrapper.find('#nama_pemesan').exists()).toBe(true);
  });

  it('Tes kolom waktu pemesanan', () => {
    expect(wrapper.find('#waktu_pemesanan').exists()).toBe(true);
  });

  it('Tes kolom status bayar', () => {
    expect(wrapper.find('#status_bayar').exists()).toBe(true);
  });

  it('Tes kolom aksi', () => {
    expect(wrapper.find('#aksi').exists()).toBe(true);
  });
});
