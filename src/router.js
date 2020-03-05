import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Pengumuman from './components/Pengumuman.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/surat',
      name: 'surat',
      component: null,
    },
    {
      path: '/pengumuman',
      name: 'pengumuman',
<<<<<<< HEAD
      component: Pengumuman,
    },
    {
      path: '/login',
      name: 'login',
      component: null,
    },
    {
      path: '/buatakun',
      name: 'buatakun',
=======
>>>>>>> 02f9fd458ec0b9cdf198b3cdab98c6a3e4c5fe99
      component: null,
    },
  ],
});
