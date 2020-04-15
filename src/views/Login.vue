<template>
  <div id="login-page" class="page-container" style="padding-top:0px!important">
    <h1>Masuk</h1>
    <div class="login-container">
      <!--
        v-model -> Value yang di-passing ke variabel "username" dan "password"
        di dalam <script>, bisa dipakai untuk keperluan backend-nya. Lebih
        jelasnya lihat console.log ketika klik "Masuk"
       -->
      <!-- USERNAME -->
      <div class="username-class">
        <h2 class="font-id" id="username-id">Username:</h2>
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
      <p>Tidak punya akun?</p>
      <button class="bottom-buttons" id="buat-akun">Buat Akun</button>
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

      request['username'] = this.username;
      request['password'] = this.password;

      axios.post('/sso/obtain-user-info/', request)
          .then((response) => {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('is_admin', response.data.is_admin);
            localStorage.setItem('is_asdos', response.data.is_asdos);
            localStorage.setItem('role', response.data.role);
            localStorage.setItem('username', this.username);

            window.location.replace('/');
          })
          .catch((error) => {
            this.message_seen = true;
          });
    },
  },
};
</script>

<style>
#login-page {
  paddding: 0 !important;
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
  width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: fit-content;
}
input {
  padding: 15px;
  border-radius: 10px;
  border-style: none;
  width: 400px;
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
#sso-link {
  color: black;
  font-weight: bolder;
  text-decoration: none;
}
.bottom-buttons {
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
