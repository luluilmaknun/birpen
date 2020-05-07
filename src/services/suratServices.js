import api from '@/services/api';

export default {
  fetchStatusSurat() {
    return api.get('permohonan-surat/status-surat/');
  },
  fetchStatusBayar() {
    return api.get('permohonan-surat/status-bayar/');
  },
  updateStatusBayar(pesanan, request) {
    return api.patch('permohonan-surat/' +
    'pesanan/'+pesanan+'/update-status-bayar/',
    request);
  },
  updateStatusSurat(pesanan, dokumen, request) {
    return api.patch('permohonan-surat/' +
    'pesanan/'+pesanan+'/surat-akademik/'+dokumen+'/update-status/',
    request);
  },
  fetchSuratAkademik() {
    return api.get('permohonan-surat/surat-akademik/');
  },
  fetchDataPemesan() {
    return api.get('permohonan-surat/pesanan/mahasiswa-profile/');
  },
  createPesanan(request) {
    return api.post('permohonan-surat/pesanan/create/', request);
  },
};
