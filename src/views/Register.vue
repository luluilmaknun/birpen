<template>
  <div id="register-page" class="page-container"
    style="padding-top:0px!important">

    <h1>Buat Akun Alumni</h1>

    <div class="register-container">

      <!-- USERNAME -->
      <div id="username-input-container">
        <h2 class="font-id" id="username-id">Username:</h2>
        <input class="username-input" v-model="username"
        placeholder="username" id="username"
        @keyup.enter="preRegister()">
      </div>

      <!-- EMAIL -->
      <div id="email-input-container">
        <h2 class="font-id" id="email-id">Email:</h2>
        <input class="email-input" v-model="email"
        placeholder="email" id="email" type="email"
        @keyup.enter="preRegister()">
      </div>

      <!-- PASSWORD -->
      <div id="password-input-container">
        <h2 class="font-id" id="password-id">Password:</h2>
        <input class="password-input" :type="'password'"
        v-model="password" placeholder="password"
        @keyup.enter="preRegister()" id="password">
      </div>

      <!-- KONFIRMASI PASSWORD -->
      <div id="password-input-container">
        <h2 class="font-id" id="confirm-password-id">Konfirmasi Password:</h2>
        <input class="password-input" :type="'password'"
        v-model="confirm_password" placeholder="Konfirmasi Password"
        @keyup.enter="preRegister()" id="password">
      </div>

      <!-- LOGIN -->
      <span style="text-align:center;color:red"
        v-if="error">
        {{ error_message }}
      </span>

      <div class="register-button-container">
        <button class="register-button"
        v-on:click="preRegister()"
        ref="submit">DAFTAR</button>
      </div>

      <modal name="register-confirmation"
        @before-open="error_message=''"
        height="auto"
        :pivotX="0.0">
        <div class="modal-container">
          <h3>Pastikan semua data sudah benar. Apakah anda yakin?</h3>
            <div class="modal-buttons">
            <button v-on:click="register()" class="yellow-black-btn">
              Daftar
            </button>
            <button v-on:click="closeModal('register-confirmation')"
              class="black-white-btn">
              Tutup
            </button>
          </div>
        </div>
      </modal>
    </div>

    <modal name="register-popup"
    @before-open="error_message=''"
    height="auto"
    :pivotX="0.0">
    <div v-if="success_regis" class="modal-container">
      <h3>
        Berhasil membuat Akun! <br>
        Menuju halaman login...
      </h3>
    </div>

    <div v-else class="modal-container">
      <h3>{{ modal_message }}</h3>
      <div class="modal-buttons">
        <button v-on:click="goToPage('login')" class="yellow-black-btn">
          Login
        </button>
        <button v-on:click="closeModal('register-popup')"
          class="black-white-btn">
          Tutup
        </button>
      </div>
    </div>
    </modal>
  </div>
</template>

<script>
import alumniApi from '@/services/alumniServices';

export default {
  data: function() {
    return {
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      error_message: '',
      modal_message: '',
      error: undefined,
      success_regis: false,
      re_email: /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/,
    };
  },
  methods: {
    showModal(modalName) {
      this.$modal.show(modalName);
    },
    closeModal(modalName) {
      this.modal_message= '';
      this.$modal.hide(modalName);
    },
    clickRegister() {
      this.$refs.submit.click();
    },
    preRegister() {
      if (!this.username ||
         !this.email ||
         !this.password ||
         !this.confirm_password) {
        this.error_message = 'Isi semua data terlebih dahulu';
        this.error = true;
      } else {
        if (!this.validateEmail(this.email)) {
          this.error_message = 'Masukkan alamat email yang valid';
          this.error = true;
        } else if (
          !this.validatePassword(this.password, this.confirm_password)) {
          this.error_message = 'Konfirmasi password tidak sesuai';
          this.error = true;
        } else {
          this.error = false;
          this.showModal('register-confirmation');
        }
      }
    },
    register() {
      const request = {};

      if (this.error == false) {
        request['username'] = this.username;
        request['password'] = this.password;
        request['email'] = this.email;

        this.processRegister(request);
      }
    },
    processRegister(request) {
      alumniApi.registerAlumni(request)
          .then((response) => {
            this.success_regis = response.data.success;
            this.closeModal('register-confirmation');
            this.showModal('register-popup');
            setTimeout(() => this.goToPage('login'), 3000);
          })
          .catch((error) => {
            this.modal_message = error.response.data.detail;
            this.success_regis = error.response.data.success;
          });

      this.closeModal('register-confirmation');
      this.showModal('register-popup');
    },
    validateEmail(email) {
      return this.re_email.test(email);
    },
    validatePassword(thePassword, confirmPassword) {
      if (confirmPassword != thePassword) return false;
      return true;
    },
    goToPage(link) {
      this.$router.push({name: link});
    },
  },
};
</script>

<style scoped>
#register-page {
  padding: 0 !important;
  height: 100%;
  display: flex;
  justify-content: center;
}
.register-container {
  padding: 20px;
  background-color: #2D3033;
  border-radius: 20px;
  margin-top: 20px;
  line-height: 30pt;
  width: fit-content;
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
.font-id {
  font-size: 13pt;
  font-weight: bold;
}
#password-input-container,
#email-input-container {
  margin-top: 20px;
}
.register-button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}
.register-button-container button {
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
.register-button-container button:hover {
  background-color: rgb(142, 255, 157);
}
.black-white-btn {
  color: white;
  background-color: black;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 12pt;
  font-weight: bolder;
  border-style: none;
}
.yellow-black-btn {
  color: black;
  background-color: #FFDD00;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 12pt;
  font-weight: bolder;
  border-style: none;
}
.modal-container {
  text-align: center;
}
@media only screen and (max-width: 539px) {
  input {
    width: 250px;
  }
}
</style>
