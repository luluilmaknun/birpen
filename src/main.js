import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import VueModal from 'vue-js-modal';

Vue.config.productionTip = false;

// Vue.use(VueRouter);
Vue.use(VueModal);
const vue = new Vue({
  router,
  render: (h) => h(App),
});

vue.$mount('#app');
