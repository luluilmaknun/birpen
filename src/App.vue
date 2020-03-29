<template>
  <div id="app">
    <Navigate-Bar></Navigate-Bar>
    <router-view class="page-container"></router-view>
  </div>
</template>

<script>
import axios from 'axios';
import Navigation from './components/Navigation';

export default {
  components: {
    'NavigateBar': Navigation,
  },
  methods: {
    refreshToken: function() {
      const params = {
        token: localStorage.token,
      };

      const self = this;

      axios.post('/sso/refresh-token/', params)
          .then(function(response) {
            localStorage.setItem('token', response.data.token);
            if (self.$route.path === '/login') {
              self.$router.push('/');
            }
          })
    },
  },
  beforeMount() {
    this.refreshToken();
  },
  watch: {
    '$route': function(to, from) {
      this.refreshToken();
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');
* {
  margin: 0 auto;
  -webkit-transition: 0.25s;
  -moz-transition: 0.25s;
  -o-transition: 0.25s;
  transition: 0.25s;
  font-family: 'Montserrat', sans-serif;
}
.page-container {
  display:flex;
  flex-direction: column;
  align-items: center;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* color: #2c3e50; */
}
</style>
