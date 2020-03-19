<template>
  <div class="container">
    <h1>Masuk</h1>
    <div class="login-container">
      <!--
        v-model -> Value yang di-passing ke script, bisa diolah untuk
        keperluan backend-nya. Lebih jelasnya lihat console.log ketika
        klik "Masuk"
       -->
      <!-- USERNAME -->
      <div class="username-class">
        <h2 class="font-id" id="username-id">Username:</h2>
        <input class="username-input" v-model="username"
        placeholder="username">
      </div>
      <!-- PASSWORD -->
      <div class="password-class">
        <h2 class="font-id" id="password-id">Password:</h2>
        <input class="password-input" :type="'password'"
        v-model="password" placeholder="password">
      </div>
      <!-- LOGIN -->
      <div class="login-class">
        <button class="login-button" v-on:click="login()">Masuk</button>
      </div>
    </div>
    <div class="hidden-div">
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      // console.log(this.username);
      // console.log(this.password);
    },
  },
};
</script>

<style>
.container {
  margin-top: 50px;
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
  border-style: solid;
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
</style>
