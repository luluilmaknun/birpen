import api from '@/services/api';

export default {
  fetchStatusSurat() {
    return api.get('permohonan-surat/status-surat/');
  },
  fetchStatusBayar() {
    return api.get('permohonan-surat/status-bayar/');
  },
  updateStatusBayar(request, pesanan) {
    return api.patch('permohonan-surat/' +
    'pesanan/'+pesanan+'/update-status-bayar/',
    request);
  },
  updateStatusSurat(request, pesanan, dokumen) {
    return api.patch('permohonan-surat/' +
    'pesanan/'+pesanan+'/surat-akademik/'+dokumen+'/update-status/',
    request);
  },
};
