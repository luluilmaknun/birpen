<template>
  <div id="unduh-karya-akhir" class="page-container">
    <h2 class="title">
      Unduh Dokumen Kelengkapan
      <br>
      Sidang Karya Akhir
    </h2>

    <div class="menu-container">
      <div class="menu-unduh-list">
        <button v-for="surat in surat_karya_akhir"
          class="btn unduh-item" :key="surat.nama"
          @click="goToPage(surat.link)">
          {{ surat.nama }}
        </button>
      </div>

      <div class="button-container">
        <button id="edit-data" class="btn btn-yellow"
          @click="goToPage('sidang-akhir')">
          Ubah Data
        </button>

        <button id="unduh-semua" class="btn btn-yellow"
          @click="goToPage('<LINK-UNDUH-SEMUA>')">
          Unduh Semua
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import karyaAkhirApi from '@/services/karyaAkhirServices';

export default {
  name: 'UnduhDokumenKaryaAkhir',
  data() {
    return {
      surat_karya_akhir: [],
    };
  },
  created() {
    karyaAkhirApi.readDataKaryaAkhir(localStorage.getItem('username'))
        .then((d) => {
          this.fetchData();
        }).catch((e) => {
          this.goToPage('sidang-akhir');
        });
  },
  methods: {
    fetchData() {
      karyaAkhirApi.fetchDaftarSuratKaryaAkhir().then(
          (d) => {
            for (let i=0; i<d.data.surat_karya_akhir.length; i++) {
              this.$set(
                  this.surat_karya_akhir,
                  i,
                  d.data.surat_karya_akhir[i],
              );

              const namaSurat =
                this.surat_karya_akhir[i]['nama'].split(' ').join('-');
              this.surat_karya_akhir[i]['link'] = namaSurat.toLowerCase();
            }
          }
      );
    },
    goToPage(name) {
      this.$router.push({name: name});
    },
  },
};
</script>

<style scoped>
.page-container {
  height: 100%;
  padding: 3%;
  box-sizing: border-box;
}
h2.title {
  font-family: 'Montserrat', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 27px;
  line-height: 40px;
  color: black;
  margin-top: 10px;
  text-align: center;
}
.menu-container {
  background: #2D3033;
  color: white;
  margin: 30px;
  padding: 10px 40px;
  border-radius: 18px;
  width: 380px;
  display: flex;
  flex-direction: column;
}
.menu-unduh-list {
  display: flex;
  flex-direction: column;
  margin: 8px 0;
}
.btn {
  cursor: pointer;
  word-break: break-word;
  border: 0;
  font-size: 15px;
}
.unduh-item {
  transition: 0s color;
  width: 100%;
  margin: 15px 0;
  background: #D8DADB;
  border-radius: 46.5px;
  padding: 9px 20px;
  font-weight: bold;
  line-height: 23px;
  color: black;
}
.btn-yellow {
  background: #FFDD00;
  border-radius: 60.5px;
}
.button-container {
  width: 100%;
  display: flex;
}
.button-container .btn {
  padding: 12px 25px;
  font-weight: bold;
  margin: 20px auto;
  width: 170px;
}
</style>
