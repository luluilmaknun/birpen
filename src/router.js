import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Login from '@/views/Login.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
import AsdosPage from '@/views/AsdosPage.vue';
import Pengumuman from '@/views/Pengumuman.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/surat/',
      name: 'surat',
      component: null,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/',
      name: 'pengumuman',
      component: Pengumuman,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/create/',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/:pk_key/edit/',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/login/',
      name: 'login',
      component: Login,
      meta: {
        guest: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/sso/logout/',
      name: 'logout',
      component: null,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/register/',
      name: 'register',
      component: null,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/asisten/',
      name: 'asisten',
      component: AsdosPage,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/asdos/',
      name: 'asdos',
      component: AsdosPage,
      pathToRegexpOptions: {strict: true},
    },
  ],
});

router.beforeEach((to, from, next) => {
  const withoutTrailingSlash = RegExp('^.*[^/]$');

  if (withoutTrailingSlash.test(to.fullPath)) {
    next(to.fullPath + '/');
  }

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
