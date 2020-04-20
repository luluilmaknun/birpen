import api from '@/services/api';

export default {
  registerAlumni(request) {
    return api.post('alumni/register/', request);
  },
  toggleBlockAlumni(username, request) {
    return api.patch('alumni/'+username+'/block/', request);
  },
};
