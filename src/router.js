import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Pengumuman from '@/views/Pengumuman.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';

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
      component: null,
    },
    {
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
    },
    {
      path: '/pengumuman/:pk_key/edit',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
    },
  ],
});
