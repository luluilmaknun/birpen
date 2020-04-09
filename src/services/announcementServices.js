import api from '@/services/api';

export default {
  getAnnouncement(key) {
<<<<<<< HEAD
    return api.get('pengumuman/'+key);
=======
    return api.get('pengumuman/'+key+'/');
>>>>>>> c6465f5f2f779f0fb0a29e2be10f00e69353045f
  },
  editAnnouncement(key, request) {
    return api.put('pengumuman/'+key+'/edit/', request);
  },
  createAnnouncement(request) {
    return api.post('pengumuman/create/', request);
  },
};
