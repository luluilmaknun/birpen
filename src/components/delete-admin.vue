<template>
  <div>
    <modal v-bind:name=this.deleted_admin_username
    @before-open="error_message=''"
    height="auto"
    :pivotX="0.0">
    <div class="modal-container">
        <div class="warning-msg">
          <h1 id="title-in-pop">Apakah anda yakin akan menghapus
          <strong>{{ this.deleted_admin_username }}</strong>
          sebagai admin?</h1>
          <p id="error-message">{{ error_message }}</p>
        </div>
        <div class="modal-buttons">
          <button v-on:click="click_hapus_conf" class="red-white-btn"
            id="hapus_conf">Hapus</button>
          <button v-on:click="click_tidak" class="black-white-btn"
            id="tidak">Tidak</button>
        </div>
    </div>
    </modal>

    <button class="remove-button" id="remove-btn"
    v-on:click="click_hapus">Hapus</button>

  </div>
</template>

<script>
import adminServices from '@/services/adminServices';

export default {
  name: 'delete-admin',
  data: function() {
    return {
      'error_message': 'd',
    };
  },
  props: {
    deleted_admin_username: String,
  },
  methods: {
    click_hapus: function() {
      this.$modal.show(this.deleted_admin_username);
    },
    click_tidak: function() {
      this.$modal.hide(this.deleted_admin_username);
    },
    click_hapus_conf: function() {
      adminServices.deleteAdmin(this.deleted_admin_username)
          .then((result) => {
            this.$router.go();
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
  margin-top: 10px;
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

.remove-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: #E63946;
  background-color: #E63946;
  border-radius: 1000px;
}

.remove-button:hover {
  background-color: white;
  color: #E63946;
}

#title-in-pop {
  color:black;
  font-size: 15pt;
  font-weight: 500;
  text-align: center;
}

.red-white-btn {
  color: white;
  background-color: #E63946;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 10pt;
  font-weight: bolder;
  border-style: none;
}

.black-white-btn {
  color: white;
  background-color: black;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 10pt;
  font-weight: bolder;
  border-style: none;
}

#error-message {
  color: red;
  font-size: 10pt;
  font-weight: bold;
  margin-top: 10pt;
  text-align: center;
}
</style>
