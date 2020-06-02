import api from '@/services/api';

export default {
  fetchJenisKaryaAkhir() {
    return api.get('karya-akhir/jenis-karya-akhir/');
  },
  readDataKaryaAkhir(username) {
    return api.get('karya-akhir/'+username+'/');
  },
  editDataKaryaAkhir(request) {
    return api.put('karya-akhir/edit/', request);
  },
  createDataKaryaAkhir(request) {
    return api.post('karya-akhir/create/', request);
  },
  getMahasiswaProfile() {
    return api.get('karya-akhir/get-profile/');
  },
  fetchDetail(username) {
    return api.get('karya-akhir/'+username+'/');
  },
};
