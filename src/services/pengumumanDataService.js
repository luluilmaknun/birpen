import api from '@/service/api';

export default {
  fetch() {
    return api.get('pengumuman/get-pengumuman');
  },
};