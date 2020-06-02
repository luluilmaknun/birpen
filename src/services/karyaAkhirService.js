import api from '@/services/api';

export default {
  fetchJenisKaryaAkhir() {
    return api.get('karya-akhir/surat/');
  },
  readDataKaryaAkhir(username) {
    return api.get('karya-akhir/'+username+'/');
  },
  editDataKaryaAkhir(request) {
    return api.put('karya-akhir/edit/', request);
  },
  createDataKaryaAkhir() {
    return api.post('karya-akhir/post/', request);
  }
};
