import Vue from 'vue';
import Router from 'vue-router';
import Pengumuman from './components/Pengumuman.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/pengumuman',
      name: 'pengumuman',
      component: Pengumuman,
    },
  ],
});
