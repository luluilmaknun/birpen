import api from '@/services/api';

export default {
  createAnnouncement(request) {
    return api.post('pengumuman/create/', request);
  },
};
