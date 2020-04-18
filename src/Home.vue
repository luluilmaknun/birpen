<template>
  <div id="app" class="home">
    <h2 class="title_home">Menu Utama</h2>
    <div class="home-button-container">
        <div id="button_surat" class="home-button"
            @click="goToPage('/surat')">
            <img src="./assets/images/mail_1.png" class="home-button-image"
            alt="Klik untuk layanan surat"/>
           Layanan Dokumen Akademik
        </div>

        <div id="button_pengumuman" class="home-button"
            @click="goToPage('/pengumuman/')">
            <img src="./assets/images/shout_1.png" class="home-button-image"
            alt="Klik untuk melihat pengumuman" />
           Pengumuman Perkuliahan
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',

  methods: {
    goToPage(link) {
      this.$router.push({path: link});
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');

body, html {
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app {
  height: 100%;
}
h2.title_home {
  font-family: 'Montserrat', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 44px;
  color: black;
  margin-top: 5%;
}
.home {
 padding: 2%;
 height: 100%;
 box-sizing: border-box;
}
.home-button-container {
  display: flex;
  justify-content: center;
  height: 100%;
  align-items: center;
  flex-wrap: wrap;
  margin: 20px;
  width: 100%;
}
.home-button-image {
  width: 40%;
  height: auto;
  margin: 25px;
}
.home-button {
  border: 6px solid #2D3033;
  box-sizing: border-box;
  border-radius: 34px;
  padding: 55px 8px;
  margin: 3%;
  min-width: 400px;
  font-family: 'Montserrat', sans-serif;
  flex-basis: 0;
  font-weight: bold;
  font-size: 30px;
  display: flex;
  align-items: center;
  text-align: center;
  cursor: pointer;
  flex-grow: 1;
  flex-direction: column;
  max-width: 430px;
}
.home-button:hover {
  background: #FFDD00;
}
#button_pengumuman {
  margin-right: 10%;
}
#button_surat {
  margin-left: 10%;
}
@media only screen and (max-width: 1600px) {
  #button_pengumuman {
    margin-right: 2%;
  }
  #button_surat {
    margin-left: 2%;
  }
}
@media only screen and (max-width: 539px) {
  .home-button {
    min-width: 300px;
    font-size: 30px;
  }
}
</style>
