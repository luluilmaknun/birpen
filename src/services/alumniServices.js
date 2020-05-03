import api from '@/services/api';
import apiNotAuthorized from './apiNotAuthorized';

export default {
  registerAlumni(request) {
    return apiNotAuthorized.post('alumni/register/', request);
  },
  toggleBlockAlumni(username, request) {
    return api.patch('alumni/'+username+'/block/', request);
  },
  fetchAlumni() {
    return api.get('alumni/');
  },
};
