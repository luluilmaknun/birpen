import Vue from 'vue';
import Router from 'vue-router';
<<<<<<< HEAD
import Pengumuman from './components/Pengumuman.vue';
=======
import Home from '@/Home.vue';
import Delete from '@/components/delete.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
>>>>>>> PBI-1-CRUD_Pengumuman

Vue.use(Router);

export default new Router({
<<<<<<< HEAD
  routes: [
    {
      path: '/pengumuman',
      name: 'pengumuman',
      component: Pengumuman,
=======
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
      component: Delete,
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
>>>>>>> PBI-1-CRUD_Pengumuman
    },
  ],
});
