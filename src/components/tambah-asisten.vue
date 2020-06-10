<template>
  <div>
    <modal name="pop-box"
    @before-open="error_message=''"
    height="auto"
    :pivotX="0.0">
    <div class="modal-container">
        <h1 id="title-in-pop">Tambah Asisten</h1><br>
        <p id="desc-in-pop">Masukan user SSO Asisten</p><br>
        <p id="error-message">{{ error_message }}</p>
        <input class="input" type="text" id="sso_username"
          v-model="sso_username"/>
        <div class="modal-buttons">
        <button v-on:click="click_tambah" class="yellow-black-btn"
          id="tambah">TAMBAH</button>
        </div>
    </div>
    </modal>
    <button v-on:click="click_tambah_asisten" class="yellow-black-btn"
      id="tambah_asisten">
      TAMBAH ASISTEN</button>
  </div>
</template>

<script>
import asistenServices from '@/services/asistenServices';

export default {
  name: 'asisten',
  data: function() {
    return {
      'sso_username': '',
      'error_message': '',
    };
  },
  methods: {
    click_tambah_asisten: function() {
      this.$modal.show('pop-box');
    },
    click_tambah: function() {
      asistenServices.createAsisten({
        username: this.sso_username,
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

<style scoped>
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
  margin: 30px 30px;
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
  font-weight: bold;
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
