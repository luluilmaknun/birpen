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
      const token = localStorage.token;

      if (typeof(token) === 'undefined'
        || token === null || token === '') {
        return;
      }

      const params = {
        token: token,
      };

      return axios.post('/sso/refresh-token/', params)
          .then(function(response) {
            localStorage.setItem('token', response.data.token);
          })
          .catch(function(error) {
            localStorage.clear();
            window.location.replace('/sso/logout/?next=/login');
          });
    },
  },
  created: function() {
    return this.refreshToken();
  },
  watch: {
    '$route': function(to, from) {
      return this.refreshToken();
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;500;700&display=swap');
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
  margin-top: 20px !important;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* color: #2c3e50; */
}
</style>
