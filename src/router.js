import Vue from 'vue';
import Router from 'vue-router';
import VueDemo from '@/components/VueDemo';
import Messages from '@/components/Messages';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo,
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages,
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
      path: '/login',
      name: 'login',
      component: null,
    },
  ],
});
