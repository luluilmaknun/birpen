import api from '@/services/api';

export default {
  getAnnouncement(key) {
    return api.post('pengumuman/'+key+'/');
  },
  editAnnouncement(key, request) {
    return api.post('pengumuman/'+key+'/edit', request);
  },
  createAnnouncement(request) {
    return api.post('pengumuman/create', request);
  },
};
