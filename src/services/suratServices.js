import api from '@/services/api';

export default {
  fetchSuratAkademik() {
    return api.get('permohonan-surat/surat-akademik/');
  },
  fetchDataPemesan() {
    return api.get('permohonan-surat/pesanan/mahasiswa-profile/')
  }
};
