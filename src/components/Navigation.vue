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
      <label v-if="is_dosen || is_admin">
        <router-link class="nav-elem"
        ref="asisten-button" :to="{ name: 'asisten' }">
        Asisten</router-link>
      </label>

      <!-- DROPDOWN -->
      <div v-if="is_admin" id="admin-dropdown-div">
        <button id="button-admin">
          Admin actions
          <img id="dropdown-img"
          src="./../assets/images/white-arrow-png-41944.png"
          alt="Klik untuk opsi lebih lanjut" />
        </button>

        <div class="admin-dropdown-container">
          <router-link class="nav-elem" id="admin-dropdown-elem"
          ref="asisten-button" :to="{ name: 'alumni' }">
          Alumni</router-link>
          <router-link class="nav-elem" id="admin-dropdown-elem"
          ref="asisten-button" :to="{ name: 'admin' }">
          Admin</router-link>
        </div>
      </div>
    </div>

    <div class="nav-elem-container-right" id="desktop-nav">

      <label v-if="is_authenticated === false">
        <router-link class="nav-elem"
        ref="register-button" :to="{ name: 'register' }">
        Buat Akun</router-link>
        <router-link class="nav-elem" id="login-button"
        ref="login" :to="{ name: 'login' }">
        Login</router-link>
      </label>

      <label v-if="is_authenticated">
        <a id="username">{{ username }}</a>
        <a class="nav-elem"
        :href="`/sso/logout/?next=%2Fsso%2Fsave_user_info`"
        id="logout-button">
        Logout
        </a>
      </label>
    </div>

    <!-- NAVBAR WHEN WIDTH 700px -->
    <div class="nav-700px">
      <button class="toggle-dropdown"
      v-on:click="mobileView = !mobileView">
      Menu List <img id="dropdown-img"
      src="./../assets/images/white-arrow-png-41944.png"
      alt="Klik untuk opsi lebih lanjut" />
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
        (localStorage.getItem('token') ? true : false),
      is_admin:
        localStorage.getItem('is_admin') === 'true',
      is_dosen:
        localStorage.getItem('role') === 'staff',
    };
  },
};
</script>

<style scoped>
/* DROPDOWN ADMIN */
#admin-dropdown-div {
  width: fit-content;
  margin-left: 10px;
  margin-right: 10px;
}
.admin-dropdown-container {
  background-color: rgb(194, 194, 194);
  border-style: solid;
  border-color: black;
  background-color: black;
  border-radius: 10px;
  display: none;
  /* IMPORTANT FOR DROPDOWN NAVBAR */
  position: absolute;
  width: 200px;
}
#admin-dropdown-elem {
  text-decoration: none;
  padding: 5px;
}
#button-admin {
  padding: 5px;
  font-size: 20pt;
  color: white;
  background: none;
  border-style: none;
}
#admin-dropdown-div:hover .admin-dropdown-container{
  display: flex;
  flex-direction: column;
  justify-items: center;
  padding: 3px;
}
#admin-dropdown-div:hover #button-admin {
  text-decoration: underline;
}
#dropdown-img {
  height: 20px;
  width: 20px;
}


/* Navbar */
.nav-700px {
  display: none;
}
.nav-container {
  position: absolute;
  width: 100%;
  padding: 10 10;
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
  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: center;
}
#nav-dropdown {
  display: none;
}
.nav-elem {
  padding:10px 10px;
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
  background-color: white;
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
