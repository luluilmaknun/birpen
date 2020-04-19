import api from '@/services/api';

export default {
  toggleBlockAlumni(username, request) {
    return api.patch('alumni/'+username+'/block/', request);
  },
};
