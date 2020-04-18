import api from '@/services/api';

export default {
  deleteAdmin(username) {
    return api.delete('admin_birpen/'+username+'/delete/');
  },
  createAdmin(request) {
    return api.post('admin_birpen/create/', request);
  },
};
