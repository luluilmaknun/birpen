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
        (result) => Promise.resolve({
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
