<template>
  <div class="detail-pengisi-karya-akhir">
    <modal
      :name="this.username"
      @before-open="error_message=''"
      height="auto"
      width="60%"
      :pivotX="0.0"
    >
      <div class="modal-container">
        <div class="top-container">
          <h1>Detail</h1>
        </div>

        <div class="loader-container" v-if="isLoadDetail">
          <img src="@/assets/icons/loader.svg" />
        </div>

        <div class="detail-container" v-else>
          <span>Nama:</span>
          {{ this.nama }}
          <br />

          <span>NPM:</span>
          {{ this.npm }}
          <br />

          <span>Program Studi:</span>
          {{ this.program_studi }}
          <br />

          <span>Peminatan:</span>
          {{ this.peminatan_mahasiswa }}
          <br />

          <span>Jenis Karya Akhir:</span>
          {{ this.jenis_karya_akhir }}
          <br />

          <span>Jumlah SKS Diperoleh:</span>
          {{ this.sks_diperoleh }}
          <br />

          <span>Pembimbing Karya Akhir:</span>
          {{ this.pembimbing }}
          <br />

          <span>Pembimbing Karya Akhir Pendamping:</span>
          {{ this.pembimbing_pendamping }}
          <br />

          <span>Judul Karya Akhir dalam Bahasa Indonesia:</span>
          {{ this.judul_karya_id }}
          <br />

          <span>Judul Karya Akhir dalam Bahasa Inggris:</span>
          {{ this.judul_karya_en }}
          <br />
        </div>

        <div class="btm-container">
          <button class="close-btn" @click="close_detail_modal">Tutup</button>
        </div>
      </div>
    </modal>

    <button class="detail-btn" @click="open_detail_modal">Detail</button>
  </div>
</template>

<script>
import karyaAkhirAPI from '@/services/karyaAkhirServices';

export default {
  name: 'detail-karya-akhir',
  data: function() {
    return {
      nama: '',
      npm: '',
      program_studi: '',
      peminatan_mahasiswa: '',
      jenis_karya_akhir: '',
      sks_diperoleh: '',
      pembimbing: '',
      pembimbing_pendamping: '',
      judul_karya_id: '',
      judul_karya_en: '',
      isLoadDetail: false,
    };
  },
  props: {
    username: {
      type: String,
      default: 'ardho',
    },
  },
  methods: {
    open_detail_modal: function() {
      this.$modal.show(this.username);
      this.fetchDetail();
    },
    close_detail_modal: function() {
      this.$modal.hide(this.username);
    },
    fetchDetail: function() {
      this.isLoadDetail = true;
      karyaAkhirAPI.fetchDetail(this.username).then((result) => {
        const response = result.data.data_karya_akhir;

        this.isLoadDetail = false;
        this.nama = response.mahasiswa.nama;
        this.npm = response.mahasiswa.npm;
        this.program_studi = response.mahasiswa.program_studi;
        this.peminatan_mahasiswa = response.peminatan_mahasiswa;
        this.jenis_karya_akhir = response.jenis_karya_akhir;
        this.sks_diperoleh = response.sks_diperoleh;
        this.pembimbing = response.pembimbing;
        this.pembimbing_pendamping = response.pembimbing_pendamping;
        this.judul_karya_id = response.judul_karya_id;
        this.judul_karya_en = response.judul_karya_en;
      });
    },
  },
};
</script>

<style scoped>
.detail-pengisi-karya-akhir .modal-container {
  margin: 30px 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.modal-container .loader-container {
    margin: 30px;
    display: flex;
    justify-content: center;
}

.modal-container .detail-container {
  margin-left: 20px;
  margin-top: 20px;
}

.modal-container .detail-container span {
  font-weight: bold;
  line-height: 30px;
}

.modal-container .btm-container {
  margin-right: 20px;
}

button {
  background: none;
  border-style: solid;
  border-width: 2px;
  border-radius: 100px;
  color: white;
  font-weight: bolder;
  padding: 5px;
}

.close-btn {
  background-color: #e63946;
  border-color: #e63946;
}

.close-btn:hover {
  background-color: white;
  color: #e63946;
}

.detail-btn {
  background-color: #5386e8;
  border-color: #5386e8;
}

.detail-btn:hover {
  background-color: white;
  color: #5386e8;
}
</style>
