import api from '@/services/api';

export default {
  getTrackingPesanan() {
    return api.get('permohonan-surat/pesanan-surat-akademik');
  },
};
