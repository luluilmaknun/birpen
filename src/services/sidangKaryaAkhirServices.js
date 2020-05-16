import api from '@/services/api';

export default {
  getProgramStudi() {
    return api.get('karya-akhir/program-studi/');
  }
}