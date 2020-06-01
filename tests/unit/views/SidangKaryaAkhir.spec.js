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
