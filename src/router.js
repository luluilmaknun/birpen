import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Delete from '@/components/delete.vue';
import Login from '@/views/Login.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';

Vue.use(Router);

const router = new Router({
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
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/pengumuman',
      name: 'pengumuman',
      component: Delete,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/pengumuman/:pk_key/edit',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        guest: true,
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (localStorage.getItem('token') == null) {
      next({name: 'login'});
    } else {
      if (to.name == 'create-pengumuman') {
        const role = localStorage.getItem('role');
        const isAsdos = localStorage.getItem('is_asdos');
        const isAdmin = localStorage.getItem('is_admin');
        if (role == 'mahasiswa') {
          if (isAsdos == 'false' && isAdmin == 'false') {
            next({name: 'pengumuman'});
          }
        }
        next();
      } else {
        next();
      }
    }
  } else if (to.matched.some((record) => record.meta.guest)) {
    if (localStorage.getItem('token') == null) {
      next();
    } else {
      next({name: 'home'});
    }
  } else {
    next();
  }
});

export default router;
