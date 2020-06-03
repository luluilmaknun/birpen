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
        <!-- KARYA AKHIR ADMIN -->
        <div v-if="isAdmin" id="button_dokumen_sidang_akhir"
          class="menu-item" @click="goToPage('/surat/sidang/daftarKaryaAkhir')">
          <div class="menu-image-container">
            <vue-load-image>
              <img slot="image" src="@/assets/images/sidang.png"
               class="menu-icon" alt="Klik untuk menuju layanan sidang akhir" />
              <img slot="preloader" src="@/assets/icons/loader.svg"/>
            </vue-load-image>
          </div>
          <h3>Dokumen Kelengkapan Sidang Karya Akhir</h3>
        </div>
        <!--- KARYA AKHIR FORM COMPLETED -->
        <div v-else-if="isFormCompleted" id="button_dokumen_sidang_akhir"
          class="menu-item" @click="goToPage('/surat/sidang/unduh/')">
          <div class="menu-image-container">
            <vue-load-image>
              <img slot="image" src="@/assets/images/sidang.png"
               class="menu-icon" alt="Klik untuk menuju layanan sidang akhir" />
              <img slot="preloader" src="@/assets/icons/loader.svg"/>
            </vue-load-image>
          </div>
          <h3>Dokumen Kelengkapan Sidang Karya Akhir</h3>
        </div>
        <!-- KARYA AKHIR NON ADMIN -->
        <div v-else-if="!isAlumni" id="button_dokumen_sidang_akhir"
          class="menu-item" @click="goToPage('/surat/sidang/')">
          <div class="menu-image-container">
            <vue-load-image>
              <img slot="image" src="@/assets/images/sidang.png"
               class="menu-icon" alt="Klik untuk menuju layanan sidang akhir" />
              <img slot="preloader" src="@/assets/icons/loader.svg"/>
            </vue-load-image>
          </div>
          <h3>Dokumen Kelengkapan Sidang Karya Akhir</h3>
        </div>

        <div id="button_pemesanan_dokumen"
          class="menu-item" @click="goToPage('/surat/pemesanan/')">
          <div class="menu-image-container">
            <vue-load-image>
              <img slot="image"
               src="@/assets/images/pemesanan.png" class="menu-icon"
               alt="Klik untuk menuju layanan pemesanan dokumen" />
              <img slot="preloader" src="@/assets/icons/loader.svg"/>
            </vue-load-image>
          </div>
          <h3>Pemesanan Dokumen Akademik</h3>
        </div>

        <div id="button_tracking_pemesanan"
          class="menu-item" @click="goToPage('/surat/tracking/')">
          <div class="menu-image-container">
            <vue-load-image>
              <img slot="image"
               src="@/assets/images/tracking.png" class="menu-icon"
               alt="Klik untuk menuju layanan tracking pemesanan" />
              <img slot="preloader" src="@/assets/icons/loader.svg"/>
            </vue-load-image>
          </div>
          <h3>Trace & Tracking Pemesanan Dokumen Akademik</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueLoadImage from 'vue-load-image';
import karyaAkhirApi from '@/services/karyaAkhirServices';

export default {
  name: 'MainMenuSurat',
  data: function() {
    return {
      isAdmin: localStorage.getItem('is_admin') === 'true',
      isAlumni: localStorage.getItem('role') === 'alumni',
      isFormCompleted: false,
    };
  },
  created: function() {
    karyaAkhirApi.readDataKaryaAkhir(localStorage.getItem('username'))
        .then((d) => {
          this.isFormCompleted = true;
        }).catch((e) => {
          if (e.response.status == 404) {
            this.isFormCompleted = false;
          }
        });
  },
  methods: {
    goToPage(link) {
      this.$router.push({path: link});
    },
  },

  components: {
    'vue-load-image': VueLoadImage,
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
.home-surat {
  height: 100%;
  padding: 2%;
  box-sizing: border-box;
}
h2.title-home {
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
  margin: 50px;
  padding: 40px;
  border-radius: 18px;
  max-width: 400px;
}
.menu-item-list {
  display: flex;
  flex-direction: column;
}
.menu-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: 0s color;
}
.menu-item:hover {
  background: white;
  color: black;
  border-radius: 18px;
}
img.menu-icon {
  width: 87px;
  margin: 10px 16px;
}
@media only screen and (max-width: 539px) {
  h2.title-home {
    font-size: 20px;
    line-height: 30px;
  }
  h3 {
    font-size: 13px;
  }
  .menu-container {
    padding: 30px;
  }
  img.menu-icon {
    width: 65px;
  }
}
</style>
