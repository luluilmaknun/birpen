import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Delete from '@/components/delete.vue';
import Login from '@/components/Login.vue';

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
      path: '/login',
      name: 'login',
      component: Login,
    },
  ],
});
