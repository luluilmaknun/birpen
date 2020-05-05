import {shallowMount} from '@vue/test-utils';
import TrackingPesanan from '@/views/TrackingPesanan.vue';
import trackingPesananApi from '@/services/trackingPesananServices.js';

describe('Cek komponen tabel', () => {
  let vm; let wrapper;
  const trackingList = [
    {
      'nama_pemesan': 'Ardo',
      'npm_pesanan': '1706075200',
      'pk': '12',
      'status_bayar': 'Belum Bayar',
      'waktu_pemesanan': '3 Januari 2020',
    },
  ];
  beforeEach(() => {
    wrapper = shallowMount(TrackingPesanan);
    vm = wrapper.vm;
    trackingPesananApi.getTrackingPesanan = jest.fn(
        (result) => Promise.resolve({
          status: 200,
          data: {
            pesanan: trackingList,
          },
        }));
    vm.fetchTrackingPesanan();
  });

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
