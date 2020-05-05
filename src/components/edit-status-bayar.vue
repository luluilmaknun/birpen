<template>
  <div>
    <modal v-bind:name=this.id_pesanan
    @before-open="error_message=''"
    height="auto"
    width="475"
    :pivotX="0.0">
      <div class='surat-id-container'>
          <p id='id-pesanan'>ID Pesanan: {{ this.id_pesanan_display }}</p>
      </div>
      <div class="modal-container">
        <h1 id="desc-modal">Status bayar</h1>
        <select v-model="status_bayar_input">
          <option v-for='status in list_status_bayar'
            :key="status">
            {{ status }}
          </option>
        </select>
      </div>
      <div class='submit-container'>
        <p id="error-message" v-if='error_message'>{{ error_message }}</p>
        <button class="simpan-button" id="simpan-button"
        @click="updateStatusBayar">Simpan</button>
      </div>
    </modal>

    <div class="container-component-edit-status">
      <img id="pen-icon" src="../assets/icons/pencil.svg" @click="open_modal"/>
    </div>
  </div>
</template>

<script>
import suratAPI from '@/services/suratServices';

export default {
  name: 'edit-status-bayar',
  props: {
    id_pesanan: String,
  },
  created() {
    this.fetchStatusBayarList();
  },
  data: function() {
    return {
      id_pesanan_display: this.id_pesanan.padStart(6, '0'),
      error_message: '',
      status_bayar_input: this.status_surat,
      list_status_bayar: [],
    };
  },
  methods: {
    open_modal: function() {
      this.$modal.show(this.id_pesanan);
    },
    fetchStatusBayarList: function() {
      suratAPI.fetchStatusBayar().then((result) => {
        this.response = result.data;
        for (let i = 0; i < this.response.status_bayar.length; i++) {
          this.$set(
              this.list_status_bayar, i, this.response.status_bayar[i].nama
          );
        }
      });
    },
    updateStatusBayar: function() {
      suratAPI.updateStatusBayar(this.id_pesanan, {
        status_bayar: this.status_bayar_input,
      }).then((result) => {
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
  margin-left: 10px;
  margin-right: 10px;
}

.modal-buttons {
  margin-top: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.modal-container {
  margin: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.surat-id-container {
  display: inline-block;
  margin-top: 20px;
  margin-left: 20px;
  border-radius: 100px;
  background: #FFDD00;
}

.submit-container {
  margin: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.simpan-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: black;
  background-color: black;
  border-radius: 1000px;
}

.simpan-button:hover {
  background-color: white;
  color: black;
}

#error-message {
  color: red;
  font-size: 10pt;
  font-weight: bold;
  margin-bottom: 30px;
  text-align: center;
}

#desc-modal {
  color:black;
  font-size: 13pt;
  font-weight: bold;
  margin: 10px;
}

#id-pesanan {
  margin: 5px;
  font-size: 10pt;
}

.container-component-edit-status {
  cursor: pointer;
  width:auto;
  text-align:center;
  padding: 8px;
}

.container-component-edit-status:hover {
  background: #e9e9e9;
  border-radius: 100%;
}

#pen-icon {
  width: 20px;
}
</style>
