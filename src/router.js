import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Login from '@/views/Login.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
import AsdosPage from '@/views/AsdosPage.vue';
import Pengumuman from '@/views/Pengumuman.vue';
import Register from '@/views/Register.vue';

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
        requiresPrivilegeToAccessPengumuman: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/create/',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessPengumuman: true,
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
        requiresPrivilegeToAccessPengumuman: true,
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
      path: '/register/',
      name: 'register',
      component: Register,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/asisten/',
      name: 'asisten',
      component: AsdosPage,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessAsisten: true,
      },
      pathToRegexpOptions: {strict: true},
    },
  ],
});

router.beforeEach((to, from, next) => {
  const [url, param] = to.fullPath.split('?');
  const withoutTrailingSlash = RegExp('^.*[^/]$');

  if (withoutTrailingSlash.test(url)) {
    let nextUrl = url + '/';
    if (typeof(param) !== 'undefined') {
      nextUrl += '?' + param;
    }
    next(nextUrl);
    return;
  }

  const token = localStorage.token;
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (typeof(token) === 'undefined'
        || token === null || token === '') {
      next({name: 'login'});
      return;
    }
  }

  if (to.matched.some((record) => record.meta.guest)) {
    if (typeof(token) !== 'undefined'
        && token !== null && token !== '') {
      next({name: 'home'});
      return;
    }
  }

  const role = localStorage.getItem('role');
  const isAsdos = localStorage.getItem('is_asdos');
  const isAdmin = localStorage.getItem('is_admin');

  if (to.matched.some(
      (record) => record.meta.requiresPrivilegeToAccessPengumuman)) {
    if (role != 'mahasiswa' && role != 'staff'
        && isAsdos == 'false' && isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  if (to.name == 'create-pengumuman') {
    if (role != 'staff' && isAsdos == 'false' && isAdmin == 'false') {
      next({name: 'pengumuman'});
      return;
    }
  }

  if (to.name == 'asisten') {
    if (role != 'staff' && isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  next();
});

export default router;
