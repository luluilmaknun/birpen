import api from '@/services/api';

export default {
  toggleBlockAlumni(username, request) {
    return api.patch('alumni/'+username+'/blacklist/', request);
  },
};
