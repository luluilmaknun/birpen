import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import VueSessionStorage from 'vue-sessionstorage';
import VueModal from 'vue-js-modal';

import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

Vue.use(VueSessionStorage);
Vue.use(VueModal);

Vue.config.productionTip = false;

// Vue.use(VueRouter);

const vue = new Vue({
  router,
  render: (h) => h(App),
});

vue.$mount('#app');
