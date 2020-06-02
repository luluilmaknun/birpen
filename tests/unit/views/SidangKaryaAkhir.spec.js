import {shallowMount} from '@vue/test-utils';
import SidangKaryaAkhir from '@/views/SidangKaryaAkhir.vue';
import apiSidangAkhir from '@/services/sidangKaryaAkhirServices.js';

describe('test get api program studi', () => {
  let wrapper; let vm;
  const mockProdi = [
    {
      'nama': 'Ilmu Ekonomi',
    },
    {
      'nama': 'Ilmu Ekonomi Islam',
    },
    {
      'nama': 'Akutansi Terapan',
    },
    {
      'nama': 'Manajemen',
    },
    {
      'nama': 'Bisnis Islam',
    },
  ];

  beforeEach(() => {
    wrapper = shallowMount(SidangKaryaAkhir);
    vm = wrapper.vm;
    apiSidangAkhir.getProgramStudi = jest.fn(
        (result) => Promise.resolve({
          status: 200,
          data: {
            program_studi: mockProdi,
          },
        }));
    vm.fetchProgramStudi();
  });

  it('test ada response', () => {
    expect(vm.programStudi.length).toBeGreaterThan(0);
  });
});

describe('test mahasiswa karya akhir table data', () => {
  let wrapper; let vm;
  const dataMock = [
    {
      'angkatan': 'Sarung',
      'nama': 'Athallah Annafis',
      'npm': '1706075021',
      'program_studi': 'bio informatika',
      'username': 'ketber',
    },
    {
      'angkatan': 'Quanta',
      'nama': 'Gundam OO',
      'npm': '1230459402',
      'program_studi': 'Mobile suit',
      'username': 'Exia',
    },
  ];
  beforeEach(() => {
    wrapper = shallowMount(SidangKaryaAkhir);
    vm = wrapper.vm;
    apiSidangAkhir.getKaryaAkhir = jest.fn(
        () => Promise.resolve({
          status: 200,
          data: {
            mahasiswa_karya_akhir: dataMock,
          },
        }));
    vm.fetchKaryaAkhir();
  });

  it('test ada mahasiswa karya akhir', () => {
    expect(vm.karyaAkhir.length).toBe(2);
  });
});

describe('test filter karya akhir success', () => {
  let wrapper; let vm;
  const filteredMockData = [
    {
      'angkatan': 'Quanta',
      'nama': 'Gundam OO',
      'npm': '1230459402',
      'program_studi': 'Bio Informatics',
      'username': 'Exia',
    },
    {
      'angkatan': 'Sarung',
      'nama': 'azhar',
      'npm': '1230459402',
      'program_studi': 'Bio Informatics',
      'username': 'Exia',
    },
  ];
  const angkatan = '';
  const prodi = 'Bio Informatics';
  beforeEach(() => {
    wrapper = shallowMount(SidangKaryaAkhir);
    vm = wrapper.vm;
    apiSidangAkhir.filterMahasiswa = jest.fn(
        (angkatan, prodi) => Promise.resolve({
          response: 200,
          data: {
            mahasiswa_karya_akhir: filteredMockData,
          },
        }));
    vm.performFilter(angkatan, prodi);
  });
  it('test filter loaded', () => {
    expect(vm.isFilterLoaded).toBe(true);
    expect(vm.filteredKaryaAkhir.length).toBeGreaterThan(0);
  });
});

// PAGINATION TEST
describe('test fetch pagination', () => {
  const wrapper = shallowMount(SidangKaryaAkhir);
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
  const wrapper = shallowMount(SidangKaryaAkhir);
  const vm = wrapper.vm;
  const pageNumber = 1;
  const pagedList = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1]]; // length = 10
  vm.renderPagination(pageNumber, pagedList);
  const result = vm.renderPagedList;
  expect(result.length).toBe(7);
});

describe('first and last button pagination function test', () => {
  const wrapper = shallowMount(SidangKaryaAkhir);
  const vm = wrapper.vm;
  it('test first page function', () => {
    vm.toFirstPage();
    expect(vm.pageNumber).toBe(1);
  });
  it('test last page function', () => {
    vm.pagedList = [1, 1, 1, 1];
    const last = vm.pagedList.length;
    vm.toLastPage();
    expect(vm.pageNumber).toBe(last);
  });
});

describe('test next prev button visibility', () => {
  const wrapper = shallowMount(SidangKaryaAkhir);
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
