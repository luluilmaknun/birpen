import {shallowMount} from '@vue/test-utils';
import TrackingPesanan from '@/views/TrackingPesanan.vue';

describe('Cek komponen tabel', () => {
  const wrapper = shallowMount(TrackingPesanan);

  it('Tes kolom id pesanan', () => {
    expect(wrapper.find('#id_pesanan').exists()).toBe(true);
  });

  it('Tes kolom nama mahasiswa', () => {
    expect(wrapper.find('#nama_mahasiswa').exists()).toBe(true);
  });

  it('Tes kolom waktu pemesanan', () => {
    expect(wrapper.find('#nama_mahasiswa').exists()).toBe(true);
  });

  it('Tes kolom status bayar', () => {
    expect(wrapper.find('#status_bayar').exists()).toBe(true);
  });

  it('Tes kolom status surat', () => {
    expect(wrapper.find('#status_surat').exists()).toBe(true);
  });

  it('Tes kolom aksi', () => {
    expect(wrapper.find('#aksi').exists()).toBe(true);
  });
});
