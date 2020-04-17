import api from '@/services/api';

export default {
  createAdmin(request) {
    return api.post('admin_birpen/create/', request);
  },
};
