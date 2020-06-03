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

describe('test fungsi dateTime', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  it('test modify date function', () => {
    const defaultDateTime = '2020-05-06T06:39:12.00+07:00';
    const result = vm.modifyDateTime(defaultDateTime);
    expect(result).toBe('06 Mei 2020');
  });
  it('test get date function', () => {
    const datetime = '2020-05-06 06:39:12';
    const result = vm.getDate(datetime);
    expect(result).toBe('06 Mei 2020');
  });
});

describe('test fungsi get nama bulan', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  const monthNumber = 2;
  const result = vm.getMonthName(monthNumber);
  expect(result).toBe('Februari');
});

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

describe('test fetch pagination', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  it('first case', () => {
    const theList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; // length = 10
    const pagedList = [];
    vm.fetchPagination(theList, pagedList);
    expect(pagedList.length).toBe(2);
  });
  it('second case', () => {
    const theList = [1, 1, 1, 1, 1, 1, 1]; // length = 7
    const pagedList = [];
    vm.fetchPagination(theList, pagedList);
    expect(pagedList.length).toBe(1);
  });
});

describe('test render pagination', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  const pageNumber = 1;
  const pagedList = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1]]; // length = 10
  vm.renderPagination(pageNumber, pagedList);
  const result = vm.renderPagedTrackingList;
  expect(result.length).toBe(7);
});

describe('first and last button pagination function test', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  it('test first page function', () => {
    vm.toFirstPage();
    expect(vm.pageNumber).toBe(1);
  });
  it('test last page function', () => {
    vm.pagedTrackingList = [1, 1, 1, 1];
    const last = vm.pagedTrackingList.length;
    vm.toLastPage();
    expect(vm.pageNumber).toBe(last);
  });
});

describe('test next prev button visibility', () => {
  const wrapper = shallowMount(TrackingPesanan);
  const vm = wrapper.vm;
  let pagedList; let pageNumber;
  let nextButton; let prevButton;
  let firstPageButton; let lastPageButton;
  it('case pertama', () => {
    nextButton = wrapper.find('#next-button');
    prevButton = wrapper.find('#prev-button');
    firstPageButton = wrapper.find('#first-page-button');
    lastPageButton = wrapper.find('#last-page-button');
    pagedList = [];
    pageNumber = 1;
    vm.checkPaginationButton(pageNumber, pagedList);
    expect(prevButton.isVisible()).toBe(true);
    expect(nextButton.isVisible()).toBe(true);
    expect(firstPageButton.isVisible()).toBe(true);
    expect(lastPageButton.isVisible()).toBe(true);
  });
  it('case kedua', () => {
    nextButton = wrapper.find('#next-button');
    prevButton = wrapper.find('#prev-button');
    firstPageButton = wrapper.find('#first-page-button');
    lastPageButton = wrapper.find('#last-page-button');
    pagedList = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1]]; // length = 2
    pageNumber = 1;
    vm.checkPaginationButton(pageNumber, pagedList);
    expect(prevButton.isVisible()).toBe(false);
    expect(nextButton.isVisible()).toBe(false);
    expect(firstPageButton.isVisible()).toBe(false);
    expect(lastPageButton.isVisible()).toBe(false);
  });
  it('case ketiga', () => {
    nextButton = wrapper.find('#next-button');
    prevButton = wrapper.find('#prev-button');
    firstPageButton = wrapper.find('#first-page-button');
    lastPageButton = wrapper.find('#last-page-button');
    pagedList = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1]]; // length = 2
    pageNumber = 2;
    vm.checkPaginationButton(pageNumber, pagedList);
    expect(nextButton.isVisible()).toBe(true);
    expect(prevButton.isVisible()).toBe(false);
    expect(firstPageButton.isVisible()).toBe(false);
    expect(lastPageButton.isVisible()).toBe(true);
  });
  it('case keempat', () => {
    nextButton = wrapper.find('#next-button');
    prevButton = wrapper.find('#prev-button');
    firstPageButton = wrapper.find('#first-page-button');
    lastPageButton = wrapper.find('#last-page-button');
    pagedList = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]];
    pageNumber = 2;
    vm.checkPaginationButton(pageNumber, pagedList);
    expect(nextButton.isVisible()).toBe(false);
    expect(prevButton.isVisible()).toBe(true);
    expect(firstPageButton.isVisible()).toBe(true);
    expect(lastPageButton.isVisible()).toBe(false);
  });
});
