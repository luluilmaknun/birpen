<template>
  <div class="nav-container">
    <div class="nav-elem-container-left">
      <router-link id="birpen"
      ref="home-button" :to="{ name: 'home' }">
      Biro Pendidikan FEB</router-link>
      <router-link class="nav-elem"
      ref="surat-button" :to="{ name: 'surat' }">
      Surat</router-link>
      <router-link class="nav-elem"
      ref="pengumuman-button" :to="{ name: 'pengumuman' }">
      Pengumuman</router-link>

      <label v-if="is_authenticated && is_staff">
            <router-link class="nav-elem"
            ref="asisten-button" :to="{ name: 'asisten' }">
            Asisten</router-link>
          </label>
    </div>

    <div class="nav-elem-container-right" id="desktop-nav">

      <label v-if="is_authenticated === false">
        <router-link class="nav-elem"
        ref="buatAkun-button" :to="{ name: 'buat-akun' }">
        Buat Akun</router-link>
        <router-link class="nav-elem" id="login-button"
        ref="login" :to="{ name: 'login' }">
        Login</router-link>
      </label>

      <label v-if="is_authenticated">
        <a id="username">{{ username }}</a>
        <router-link class="nav-elem" id="logout-button"
        ref="logout" :to="{ name: 'logout' }">
        Logout</router-link>
      </label>
    </div>

    <!-- NAVBAR WHEN WIDTH 700px -->
    <div class="nav-700px">
      <button class="toggle-dropdown"
      v-on:click="mobileView = !mobileView">
      Menu List <img alt="dropdown-icon" id="dropdown-img"
      src="./../assets/images/white-arrow-png-41944.png"/>
      </button>

      <div class="nav-elem-container-right"
      id="mob-nav" v-show="mobileView">
        <router-link class="nav-elem"
        ref="surat-button" :to="{ name: 'surat' }">
        Surat
        </router-link>
        <router-link class="nav-elem"
        ref="pengumuman-button" :to="{ name: 'pengumuman' }">
        Pengumuman
        </router-link>
        <router-link class="nav-elem"
        ref="buatAkun-button" :to="{ name: 'buat akun' }">
        Buat Akun
        </router-link>
        <router-link class="nav-elem" id="login-button"
        ref="login" :to="{ name: 'login' }">
        Login
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mobileView: false,
      username: localStorage.getItem('username'),
      is_authenticated:
        localStorage.getItem('username') !== null,
      is_staff:
        localStorage.getItem('is_admin') === 'true' ||
        localStorage.getItem('is_asdos') === 'true',
    };
  },
};
</script>

<style scoped>
.nav-700px {
  display: none;
}
.nav-container {
  padding: 20px 20px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: black;
  flex-wrap: wrap;
}
h2 {
  font-size: 26pt;
  color: white;
}
.nav-elem-container-left {
  font-weight:900;
}
#nav-dropdown {
  display: none;
}
.nav-elem {
  padding:20px 20px;
  text-decoration: none;
  margin-left: 10px;
  margin-right: 10px;
  font-weight: normal;
  font-size: 20pt;
  color: white;
  text-align: center;
}
.nav-elem:hover {
  color: black;
  border-radius: 100px;
  padding-top: 5px;
  padding-bottom: 5px;
  text-align: center;
}
#login-button {
  color:black;
  background-color: #FFDD00;
  border-radius: 100px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
}
#login-button:hover {
  background-color: rgb(216, 187, 1);
}
#logout-button {
  color:white;
  background-color: #E63946;
  border-radius: 100px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
}
#logout-button:hover {
  background-color: rgb(202, 50, 62);
}
#username {
  color: #FFDD00;
  padding:20px 20px;
  text-decoration: none;
  margin-left: 10px;
  margin-right: 10px;
  font-weight: normal;
  font-size: 20pt;
  text-align: center;
}
#birpen {
  color: white;
  padding:20px 20px;
  text-decoration: none;
  margin-left: 10px;
  margin-right: 10px;
  font-weight: bolder;
  font-size: 20pt;
  text-align: center;
}
.dropdown-button {
  display: none;
}
@media only screen and (max-width:700px) {
  #dropdown-img {
    width: 10px;
    height: 10px;
  }
  .nav-700px {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .toggle-dropdown {
    background: none;
    border-style: none;
    color: white;
    margin-top: 5px;
  }
  #desktop-nav {
    display: none;
  }
  .nav-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .nav-elem-container-right {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .nav-elem {
    padding: 10px 10px;
    font-size: 10pt;
    margin-top: 5px;
    width: fit-content;
  }
  .nav-elem-container-left h2 {
    font-size: 15pt;
  }
  .dropdown-button {
    display: flex;
  }
  #login-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 3px;
    font-size: 10pt;
    margin-top: 10px;
  }
}
</style>
