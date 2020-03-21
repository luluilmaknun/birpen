import api from '@/services/api';

export default {
  fetch() {
    return api.get('pengumuman/get-pengumuman');
  },
};
