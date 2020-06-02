import api from '@/services/api';

export default {
  fetchDetail(username) {
    return api.get('karya-akhir/'+username+'/');
  },
};
