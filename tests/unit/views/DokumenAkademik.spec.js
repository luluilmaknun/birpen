import {shallowMount} from '@vue/test-utils';
import DokumenAkademik from '@/views/DokumenAkademik';
import suratApi from '@/services/suratServices';

suratApi.fetchDataPemesan = jest.fn(() => Promise.resolve({
  status: 200,
  data: {
    mahasiswa: {
      nama: 'Lulu',
      npm: '1706979341',
    },
  },
}));

describe('Test fetch surat akademik function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(DokumenAkademik);
    vm = wrapper.vm;

    suratApi.fetchSuratAkademik = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        surat_akademik: [
          {
            jenis_dokumen: 'Transkrip Nilai',
            harga_mahasiswa: 0,
            harga_alumni: 10000,
          },
          {
            jenis_dokumen: 'Surat Keterangan Mahasiswa',
            harga_mahasiswa: 1000,
            harga_alumni: 0,
          },
        ],
      },
    }));

    vm.fetchLetterList();
  });

  it('Cek sukses', () => {
    expect(vm.surat_akademik.length).toBe(2);
    expect(wrapper.findAll('tr').length).toBe(2 + 1);
  });
});

describe('Test fetch surat akademik function', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          surat_akademik: [
            {
              jenis_dokumen: 'Transkrip Nilai',
              harga_mahasiswa: 0,
              harga_alumni: 10000,
            },
            {
              jenis_dokumen: 'Surat Keterangan Mahasiswa',
              harga_mahasiswa: 1000,
              harga_alumni: 0,
            },
          ],
        };
      },
    });
    vm = wrapper.vm;
  });

  it('Cek increment', () => {
    const count = wrapper.find({ref: 'jumlah_1'});
    count.element.value = 1;
    count.trigger('change');

    expect(count.element.value).toBe('1');

    vm.update('increment', 0);
    count.trigger('change');

    expect(count.element.value).toBe('2');
  });

  it('Cek decrement', () => {
    const count = wrapper.find({ref: 'jumlah_1'});
    count.element.value = 2;
    count.trigger('change');

    expect(count.element.value).toBe('2');

    vm.update('decrement', 0);
    count.trigger('change');
    expect(count.element.value).toBe('1');
  });

  it('Cek decrement min value zero', () => {
    const count = wrapper.find({ref: 'jumlah_1'});
    count.element.value = 0;
    count.trigger('change');

    expect(count.element.value).toBe('0');

    vm.update('decrement', 0);
    count.trigger('change');
    expect(count.element.value).toBe('0');
  });
});

describe('Tes modal function', () => {
  const vm = shallowMount(DokumenAkademik, {
    'mocks': {
      $modal: {
        hide: jest.fn(),
        show: jest.fn(),
      },
    },
  }).vm;

  it('Tes close Modal', () => {
    vm.closeModal();
  });

  it('Tes show Modal', () => {
    vm.showModal();
  });
});

describe('Tes go to page function', () => {
  it('goToPage() method', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      'mocks': {
        $router: {
          push: jest.fn(),
        },
      },
    });

    wrapper.vm.goToPage('login');
  });
});

describe('Tes validate data function', () => {
  suratApi.createPesanan = jest.fn(() => Promise.resolve({
    status: 200,
  }));

  it('Tes success alumni', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          isAlumni: true,
          nama_pemesan: 'Lulu',
          npm_pemesan: '1706979341',
          pesanan: [
            {
              jenis_dokumen: 'Surat Keterangan Mahasiswa',
              jumlah: 2,
            },
            {
              jenis_dokumen: 'Daftar Nilai Semester',
              jumlah: 1,
            },
          ],
        };
      },
    });

    wrapper.vm.validateData();
  });

  it('Tes success non-alumni', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          isAlumni: false,
          nama_pemesan: 'Lulu',
          npm_pemesan: '1706979341',
          pesanan: [
            {
              jenis_dokumen: 'Surat Keterangan Mahasiswa',
              jumlah: 2,
            },
            {
              jenis_dokumen: 'Daftar Nilai Semester',
              jumlah: 1,
            },
          ],
        };
      },
    });

    wrapper.vm.validateData();
  });

  it('Tes fail nama dan npm belum diisi', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          nama_pemesan: '',
          npm_pemesan: '',
          pesanan: [
            {
              jenis_dokumen: 'Surat Keterangan Mahasiswa',
              jumlah: 2,
            },
            {
              jenis_dokumen: 'Daftar Nilai Semester',
              jumlah: 1,
            },
          ],
        };
      },
    });

    wrapper.vm.validateData();
  });

  it('Tes fail pesanan tidak ada', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          nama_pemesan: 'Lulu',
          npm_pemesan: '1706979341',
          pesanan: [],
        };
      },
    });

    wrapper.vm.validateData();
  });

  it('Tes fail request letter error backend', () => {
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          nama_pemesan: 'Lulu',
          npm_pemesan: '170697931',
          pesanan: [
            {
              jenis_dokumen: 'Surat Keterangan Mahasiswa',
              jumlah: 2,
            },
            {
              jenis_dokumen: 'Daftar Nilai Semester',
              jumlah: 1,
            },
          ],
        };
      },
    });

    const error = new Error('error');
    error.response = {
      status: 400,
      data: {
        success: false,
        detail: 'Data tidak valid',
      },
    };

    suratApi.createPesanan = jest.fn(() => Promise.reject(error));

    wrapper.vm.validateData();

    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.error_message).toBe('Data tidak valid');
    });
  });
});

describe('Tes summarize function', () => {
  it('Tes functionality', () =>{
    const wrapper = shallowMount(DokumenAkademik, {
      data() {
        return {
          nama_pemesan: 'Lulu',
          npm_pemesan: '170697931',
          temp_pesanan: {
            'Surat mencinta': {
              'jumlah': 10,
              'harga': 100,
            },
            'Surat ga apa2': {
              'jumlah': 0,
              'harga': 0,
            },
          },
        };
      },
      'mocks': {
        $modal: {
          hide: jest.fn(),
          show: jest.fn(),
        },
      },
    });

    wrapper.vm.summarize();
  });
});
