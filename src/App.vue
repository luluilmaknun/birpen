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
    refreshData: function() {
      const token = localStorage.token;

      if (typeof(token) === 'undefined'
        || token === null || token === '') {
        return;
      }

      return axios.get('/sso/refresh-data/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
          .then(function(response) {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('username', response.data.username);
            localStorage.setItem('role', response.data.role);
            localStorage.setItem('is_admin', response.data.is_admin);
            localStorage.setItem('is_asdos', response.data.is_asdos);
          })
          .catch(function(error) {
            localStorage.clear();
            window.location.replace('/sso/logout/?next=/login');
          });
    },
  },
  created: function() {
    return this.refreshData();
  },
  watch: {
    '$route': function(to, from) {
      return this.refreshData();
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
  padding-top: 100px !important;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* color: #2c3e50; */
}
</style>
