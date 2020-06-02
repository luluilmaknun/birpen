<template>
  <div class="main-container-edit-status-surat">
    <modal v-bind:name=this.jenis_dokumen
    @before-open="error_message=''"
    height="auto"
    width="475"
    :pivotX="0.0">
      <div class='surat-id-container'>
          <p id='id-pesanan'>ID Pesanan: {{ this.id_pesanan_display }}</p>
      </div>
      <div class="modal-container">
        <h1 id="desc-modal">Status surat</h1>
        <select v-model="status_surat_input">
          <option v-for='status in list_status_surat'
            :key="status">
            {{ status }}
          </option>
        </select>
      </div>
      <div class='submit-container'>
        <p id="error-message" v-if='error_message'>{{ error_message }}</p>
        <button class="simpan-button" id="simpan-button"
        @click="updateStatusSurat">Simpan</button>
      </div>
    </modal>

    <div class="container-component-edit-status">
      <img id="pen-icon" src="../assets/icons/pencil.svg"
        alt="Klik untuk edit status surat" @click="open_modal"/>
    </div>
  </div>
</template>

<script>
import suratAPI from '@/services/suratServices';

export default {
  name: 'edit-status-surat',
  props: {
    id_pesanan: String,
    jenis_dokumen: String,
    status_surat: String,
  },
  created() {
    this.fetchStatusSuratList();
  },
  data: function() {
    return {
      id_pesanan_display: this.id_pesanan.padStart(6, '0'),
      error_message: '',
      status_surat_input: this.status_surat,
      list_status_surat: [],
    };
  },
  methods: {
    open_modal: function() {
      this.$modal.show(this.jenis_dokumen);
    },
    fetchStatusSuratList: function() {
      suratAPI.fetchStatusSurat().then((result) => {
        this.response = result.data;
        for (let i = 0; i < this.response.status_surat.length; i++) {
          this.$set(
              this.list_status_surat, i, this.response.status_surat[i].nama
          );
        }
      });
    },
    updateStatusSurat: function() {
      suratAPI.updateStatusSurat(this.id_pesanan, this.jenis_dokumen, {
        status_surat: this.status_surat_input,
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
.main-container-edit-status-surat {
  margin: 0;
}

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
