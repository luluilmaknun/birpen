<template>
  <div id="app" class="home-surat">
    <h2 class="title-home">
      Selamat Datang di
      <br>
      Layanan Dokumen Akademik Biro Pendidikan
      <br>
      Fakultas Ekonomi dan Bisnis
      <br>
      Universitas Indonesia
    </h2>

    <div class="menu-container">
      <div class="menu-item-list">
        <div id="button_dokumen_sidang_akhir"
          class="menu-item" @click="goToPage('/surat/sidang/')">
          <div class="menu-image-container">
            <img class="home-surat-menu" />
          </div>
          <h3>Dokumen Kelengkapan Sidang Karya Akhir</h3>
        </div>

        <div id="button_pemesanan_dokumen"
          class="menu-item" @click="goToPage('/surat/pemesanan/')">
          <div class="menu-image-container">
            <img class="home-surat-menu" />
          </div>
          <h3>Pemesanan Dokumen Akademik</h3>
        </div>

        <div id="button_tracking_pemesanan"
          class="menu-item" @click="goToPage('/surat/tracking/')">
          <div class="menu-image-container">
            <img class="home-surat-menu" />
          </div>
          <h3>Trace & Tracking Pemesanan Dokumen Akademik</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainMenuSurat',

  methods: {
    goToPage(link) {
      this.$router.push({path: link});
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');

body, html {
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.home_surat {
  height: 100%;
  padding: 2%;
  height: 100%;
  box-sizing: border-box;
}
h2.title_home {
  font-family: 'Montserrat', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 27px;
  line-height: 40px;
  color: black;
  margin-top: 10px;
  text-align: center;
}
@media only screen and (max-width: 1600px) {
}
@media only screen and (max-width: 539px) {
}
</style>
