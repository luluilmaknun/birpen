import api from '@/services/api';

export default {
  deleteAdmin(username) {
    return api.delete('admin_birpen/'+username+'/delete/');
  },
};
