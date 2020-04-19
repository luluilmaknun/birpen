import api from '@/services/api';

export default {
  toggleBlockAlumni(request) {
    return api.patch('alumni/blacklist/', request);
  },
};
