import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Delete from '@/components/delete.vue';
import Login from '@/views/Login.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
import AsdosPage from '@/views/AsdosPage.vue';

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
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/asdos',
      name: 'asdos',
      component: AsdosPage,
    },
  ],
});
