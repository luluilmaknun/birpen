import api from '@/services/api';

export default {
  fetchDaftarSuratKaryaAkhir() {
    return api.get('karya-akhir/surat/');
  },
}
