import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';

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
      path: '/pengumuman/create',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
    },
  ],
});
