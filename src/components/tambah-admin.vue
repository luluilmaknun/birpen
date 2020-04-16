<template>
  <div>
    <modal name="pop-box"
    :height="350"
    :pivotX="0.0" id = "center-div">
    <div class="modal-container">
        <h1 id="title-in-pop">Tambah Admin</h1><br>
        <p id="desc-in-pop">Masukan user SSO Admin</p><br>
        <p id="error-message">{{ error_message }}</p>
        <input class="input" type="text" id="admin_username"
          v-model="admin_username"/>
        <div class="modal-buttons">
        <button v-on:click="click_tambah" class="yellow-black-btn"
          id="tambah">TAMBAH</button>
        </div>
    </div>
    </modal>
    <button v-on:click="click_tambah_admin" class="yellow-black-btn"
      id="tambah_admin">
      TAMBAH ADMIN</button>
  </div>
</template>

<script>
import adminServices from '@/services/adminServices';

export default {
  name: 'admin',
  data: function() {
    return {
      'admin_username': '',
      'error_message': '',
    };
  },
  methods: {
    click_tambah_admin: function() {
      this.$modal.show('pop-box');
    },
    click_tambah: function() {
      adminServices.createAdmin({
        username: this.admin_username,
      }).then((result) => {
        this.$router.go({
          path: '/',
          force: true,
        });
      }).catch((error) => {
        this.error_message = error.response.data.detail;
      });
    },
  },
};
</script>

<style>
.modal-buttons button {
  margin-left: 20px;
  margin-right: 20px;
}

.modal-buttons {
  margin-top: 15px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.modal-container {
  margin: 70px 70px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.yellow-black-btn {
  color:black;
  background-color: #FFDD00;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 10pt;
  font-weight: bolder;
  border-style: none;
}

#title-in-pop {
  color:black;
  font-size: 35pt;
  font-weight: bold;
}

#desc-in-pop {
  color:black;
  font-size: 15pt;
  font-weight: lighter;
}

#error-message {
  color: red;
  font-size: 10pt;
  font-weight: lighter;
  margin-bottom: 10pt;
}

input[type=text], select {
  width: 75%;
  padding: 12px 20px;
  margin: 5px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  text-align: center;
  font-size: 100%;
}

</style>
