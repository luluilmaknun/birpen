import {shallowMount} from '@vue/test-utils';
import TrackingPesanan from '@/views/TrackingPesanan.vue';
import trackingPesananApi from '@/services/suratServices.js';

describe('Cek komponen tabel', () => {
  let vm; let wrapper;
  const response = [
    {
      'nama_pemesan': 'Ardo',
      'npm_pesanan': '1706075200',
      'pk': '000012',
      'status_bayar': 'Belum Bayar',
      'waktu_pemesanan': '27 Mei 2020',
    },
  ];
  beforeEach(() => {
    wrapper = shallowMount(TrackingPesanan);
    vm = wrapper.vm;
    trackingPesananApi.getTrackingPesanan = jest.fn(
        (result) => Promise.resolve({
          status: 200,
          data: {
            pesanan: response,
          },
        }));
    vm.fetchTrackingPesanan();
    const trackingList = vm.trackingList;
    const pagedTrackingList = vm.pagedTrackingList;
    vm.fetchPagination(trackingList, pagedTrackingList);
    vm.renderPagination(1, pagedTrackingList);
  });

  it('test ada response', () => {
    expect(vm.trackingList.length).toBe(1);
  });
});


describe('test button pagination', () => {
  const wrapper = shallowMount(TrackingPesanan);

  it('test untuk button increamant', () => {
    const nextButton = wrapper.find('#next-button');
    expect(nextButton.exists()).toBe(true);
    nextButton.trigger('click');
  });

  it('test untuk button decreament', () => {
    const prevButton = wrapper.find('#prev-button');
    expect(prevButton.exists()).toBe(true);
    prevButton.trigger('click');
  });
});

describe('test fungsi modify date', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  const defaultDateTime = '2020-05-06T06:39:12.00+07:00';
  const result = vm.modifyDateTime(defaultDateTime);
  expect(result).toBe('2020-05-06 06:39:12');
});

describe('test fungsi get nama bulan', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  const monthNumber = 2;
  const result = vm.getMonthName(monthNumber);
  expect(result).toBe('Februari');
});

// describe('test fungsi get date', () => {
//   const wrapper = shallowMount(TrackingPesanan);
//   const vm = wrapper.vm;
//   const dateTime = '2020-05-06 06:39:12';
//   const result = vm.getDate(dateTime);
//   expect(result).toBe('5 Mei 2020');
// });

describe('test fungsi show detail page', () => {
  const wrapper = shallowMount(TrackingPesanan, {
    mocks: {
      $router: {
        push: jest.fn(),
      },
    },
  });
  const vm = wrapper.vm;
  global.window = Object.create(window);
  const pk = 12;
  const url = 'https://birpen.com' + '/surat/tracking/' + pk + '/detail/';
  Object.defineProperty(window, 'location', {
    value: {
      href: url,
    },
  });
  vm.showDetailPage(pk);
  expect(window.location.href).toEqual(url);
});
