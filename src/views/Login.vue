<template>
  <div id="login-page" class="page-container" style="padding-top:0px!important">
    <h1>Masuk</h1>
    <div class="login-container">
      <!-- USERNAME -->
      <div class="username-class">
        <h2 class="font-id" id="username-id">Username:</h2>
        <input class="disabled-username-input" placeholder="@" disabled>
        <input class="username-input" v-model="username"
        placeholder="username" id="uname"
        @keyup.enter="clickMasuk">
      </div>
      <!-- PASSWORD -->
      <div class="password-class">
        <h2 class="font-id" id="password-id">Password:</h2>
        <input class="password-input" :type="'password'"
        v-model="password" placeholder="password"
        @keyup.enter="clickMasuk" id="pass">
      </div>
      <!-- LOGIN -->
      <span style="text-align:center;color:red"
        v-if="message_seen">
        {{ message }}
      </span>
      <div class="login-class">
        <button class="login-button" v-on:click="login()"
        ref="submit">Masuk</button>
      </div>
    </div>
    <div class="bottom-container">
      <a class="bottom-buttons"
      :href="`/sso/login/?next=%2Fsso%2Fsave_user_info`"
      id="sso-link">
        Login with<br>SSO
      </a>
      <p>Tidak punya sso?</p>
      <a class="bottom-buttons"
      :href="`/register/`"
      id="buat-akun">
        Buat Akun<br> Alumni
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: function() {
    return {
      username: '',
      password: '',
      message: 'Username/Password salah',
      message_seen: false,
    };
  },
  methods: {
    clickMasuk() {
      this.$refs.submit.click();
    },
    login() {
      const request = {};

      request['username'] = '@' + this.username;
      request['password'] = this.password;

      axios.post('/sso/obtain-user-info/', request)
          .then((response) => {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('is_admin', response.data.is_admin);
            localStorage.setItem('is_asdos', response.data.is_asdos);
            localStorage.setItem('role', response.data.role);
            localStorage.setItem('username', response.data.username);

            window.location.replace('/');
          })
          .catch((error) => {
            this.message = error.response.data.detail;
            this.message_seen = true;
          });
    },
  },
};
</script>

<style scoped>
#login-page {
  padding: 0 !important;
  height: 100%;
  display: flex;
  justify-content: center;
}
.login-container {
  padding: 20px;
  background-color: #2D3033;
  border-radius: 20px;
  margin-top: 20px;
  line-height: 30pt;
  min-width: fit-content;
  display: flex;
  flex-direction: column;
  align-items: center;
}
input {
  padding: 15px;
  border-radius: 10px;
  border-style: none;
  width: 400px;
}
.disabled-username-input {
  width: 20px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0px;
}
.username-input {
  width: 350px;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
}
.font-id {
  font-size: 13pt;
  font-weight: bold;
}
.password-class {
  margin-top: 20px;
}
.login-class {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}
.login-class button {
  border-style: none;
  background: none;
  background-color: #D8DADB;
  color: black;
  font-weight: bolder;
  border-radius: 1000px;
  padding: 5px;
  padding-left: 10px;
  padding-right: 10px;
  font-size: 13pt;
}
.login-class button:hover {
  background-color: rgb(142, 255, 157);
}
.bottom-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
}
.bottom-container * {
  margin-left: 10px;
  margin-right: 10px;
}
.bottom-buttons {
  text-decoration: none;
  background: none;
  border-style: solid;
  border-color: #FFDD00;
  background-color: #FFDD00;
  font-weight: bolder;
  border-width: 2px;
  color: black;
  padding: 7px 20px;
  border-radius: 1000px;
  font-size: 13pt;
  text-align: center;
}
.bottom-buttons:hover {
  background-color: white;
}
</style>
