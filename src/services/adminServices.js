import api from '@/services/api';

export default {
  fetchAdmin() {
    return api.get('admin_birpen/');
  },
  deleteAdmin(username) {
    return api.delete('admin_birpen/'+username+'/delete/');
  },
  createAdmin(request) {
    return api.post('admin_birpen/create/', request);
  },
};
