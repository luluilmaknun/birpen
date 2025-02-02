import api from '@/services/api';

export default {
  getAnnouncement(key) {
    return api.get('pengumuman/'+key+'/');
  },
  editAnnouncement(key, request) {
    return api.put('pengumuman/'+key+'/edit/', request);
  },
  createAnnouncement(request) {
    return api.post('pengumuman/create/', request);
  },
  getAnnouncementDefault() {
    return api.get('pengumuman/get-pengumuman');
  },
  getAnnouncementFiltered(tanggal) {
    return api.get('pengumuman/?tanggal='+tanggal);
  },
};
