import Vue from 'vue';
import Home from '@/Home.vue';
import router from '@/router';

Vue.config.productionTip = false;

// Vue.use(VueRouter);

const vue = new Vue({
  router,
  render: (h) => h(Home),
});

vue.$mount('#app');
