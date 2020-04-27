<template>
  <div>
    <modal v-bind:name=this.id_pesanan
    @before-open="error_message=''"
    height="auto"
    width="475"
    :pivotX="0.0">
      <div class='surat-id-container'>
        <button disabled class="surat-id-component">
          ID Pesanan: {{ this.id_pesanan }}
        </button>
      </div>
      <div class="modal-container">
        <h1 id="desc-modal">Status bayar</h1>
        <select v-model="status_bayar_input">
          <option v-for="status in status_bayar_dd"
            :key=status>
            {{ status }}
          </option>
        </select>
        <h1 id="desc-modal">Status surat</h1>
        <select v-model="status_surat_input">
          <option v-for='status in status_surat_dd'
            :key="status">
            {{ status }}
          </option>
        </select>
      </div>
      <div class='submit-container'>
        <p id="error-message" v-if='error_message'>{{ error_message }}</p>
        <button class="simpan-button" id="id-simpan-button"
        @click="close_modal">Simpan</button>
      </div>
    </modal>

    <div>
      <button class="edit-status-button" id="id-edit-status-button"
      @click="open_modal">Edit status</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'edit-status-surat',
  props: {
    id_pesanan: String,
    status_bayar: String,
    status_surat: String,
  },
  data: function() {
    return {
      error_message: '',
      status_bayar_input: this.status_bayar,
      status_bayar_dd: [ // TO DO fetch dari DB Dropdown
        'Belum bayar',
        'Lunas',
      ],
      status_surat_input: this.status_surat,
      status_surat_dd: [ // TO DO fetch dari DB Dropdown
        'Menunggu paraf manager pendidikan',
        'Menunggu paraf wakil dekan 1',
        'Menunggu paraf wakil dekan',
        'Selesai',
      ],
    };
  },
  methods: {
    open_modal: function() {
      this.$modal.show(this.id_pesanan);
    },
    close_modal: function() {
      this.$modal.hide(this.id_pesanan);
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
  align-items: right;
  margin: 20px;
}

.surat-id-component {
  background-color: #FFDD00;
  border-radius: 1000px;
  color: black;
  font-weight: bolder;
}

.submit-container {
  margin: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#desc-modal {
  color:black;
  font-size: 13pt;
  font-weight: 500;
  text-align: center;
}

.edit-status-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: #206bdd;
  background-color: #206bdd;
  border-radius: 1000px;
}

.edit-status-button:hover {
  background-color: white;
  color: #206bdd;
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
</style>
