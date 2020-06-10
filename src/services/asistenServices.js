import api from '@/services/api';

export default {
  createAsisten(request) {
    return api.post('asdos/create-asisten/', request);
  },
  deleteAsisten(key, request) {
    return api.delete('asdos/'+key+'/delete/', request);
  },
  getAsisten() {
    return api.get('asdos/');
  },
};
