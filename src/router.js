import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Delete from '@/components/delete.vue';
import Login from '@/components/Login.vue';
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
      component: Delete,
      beforeEnter: (to, from, next) => {
        if (!localStorage.getItem('token')) {
          next('/sso/login/');
        }
        next();
      },
    },
    {
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
      beforeEnter: (to, from, next) => {
        const role = localStorage.getItem('role');
        const isAsdos = localStorage.getItem('is_asdos');
        const isAdmin = localStorage.getItem('is_admin');
        if (role == 'mahasiswa') {
          if (isAsdos == 'false' && isAdmin == 'false') {
            next('/pengumuman');
          }
        }
        next();
      },
    },
    {
      path: '/pengumuman/:pk_key/edit',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
      beforeEnter: (to, from, next) => {
        if (!localStorage.getItem('token')) {
          next('/sso/login/');
        }
        next();
      },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/buatakun',
      name: 'buatakun',
      component: null,
    },
  ],
});
