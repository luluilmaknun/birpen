import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';

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
      component: null,
    },
    {
      path: '/login',
      name: 'login',
      component: null,
    },
    {
      path: '/buatakun',
      name: 'buatakun',
      component: null,
    },
    {
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
    },
  ],
});
