import api from '@/services/api';

export default {
  createAsisten(request) {
    return api.post('asdos/create-asisten/', request);
  },
  deleteAsisten(request) {
    return api.delete('asdos/delete/', request);
  },
};
