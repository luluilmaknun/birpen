import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
<<<<<<< HEAD
import Login from '@/components/Login.vue';
=======
import Delete from '@/components/delete.vue';
import Login from '@/views/Login.vue';
>>>>>>> e9e104bf8fef9762e8996c0064d263c0b247073b
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
import Pengumuman from '@/views/Pengumuman.vue';

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
<<<<<<< HEAD
      component: Pengumuman,
=======
      component: Delete,
>>>>>>> e9e104bf8fef9762e8996c0064d263c0b247073b
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
    {
      path: '/sso/logout',
      name: 'logout',
      component: null,
    },
    {
      path: '/register',
      name: 'register',
      component: null,
    },
    {
      path: '/asisten',
      name: 'asisten',
      component: null,
    },
  ],
});

router.beforeEach((to, from, next) => {
  const token = localStorage.token;
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (typeof(token) === 'undefined'
        || token === null || token === '') {
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
    if (typeof(token) === 'undefined'
        || token === null || token === '') {
      next();
    } else {
      next({name: 'home'});
    }
  } else {
    next();
  }
});

export default router;
