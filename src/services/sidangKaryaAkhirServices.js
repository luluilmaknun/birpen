import api from '@/services/api';

export default {
  getProgramStudi() {
    return api.get('karya-akhir/program-studi/');
  },
  getKaryaAkhir() {
    return api.get('karya-akhir/mahasiswa/');
  },
  filterMahasiswa(angkatan, prodi) {
    // api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi
    return api.get('karya-akhir/filter-mahasiswa?angkatan=' + angkatan +
    '&prodi=' + prodi);
  },
};
