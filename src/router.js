import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
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
      component: null,
    },
    {
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
    },
    {
      path: '/pengumuman/:key/edit',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
    },
  ],
});
