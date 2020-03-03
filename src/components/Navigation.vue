<template>
    <div class="nav-container">

        <div class="nav-elem-container-left">
            <h2>
                Biro Pendidikan FEB
            </h2>
        </div>

        <div class="nav-elem-container-right">
            <router-link class="nav-elem"
            ref="surat-button" :to="{ name:'messages' }">
            Surat
            </router-link>
            <router-link class="nav-elem"
            ref="pengumuman-button" :to="{ name:'messages' }">
            Pengumuman
            </router-link>
            <router-link class="nav-elem"
            ref="buatAkun-button" :to="{ name:'messages' }">
            Buat Akun
            </router-link>
            <router-link class="nav-elem-login"
            ref="login" :to="{ name:'messages' }">
            Login
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
  components: 'Navigation',
  data() {
    return {};
  },
};
</script>


<style>
h2 {
    font-size: 26pt;
    color: white;
}

.nav-elem-container-left {
    font-weight: bolder;
}

.nav-container {
    padding: 20px 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    background-color: black;
}

.nav-spreader {
    margin-left: 20px;
}

.nav-elem {
    padding:20px 20px;
    text-decoration: none;
    margin-left: 10px;
    margin-right: 10px;
    font-weight: normal;
    font-size: 20pt;
    color: white;
}

.nav-elem:hover {
    background-color: white;
    color: black;
}

.nav-elem-login {
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 5px;
    padding-bottom: 5px;
    text-decoration: none;
    margin-left: 10px;
    margin-right: 10px;
    font-size: 20pt;
    color: black;
    background: yellow;
    border-color: yellow;
    border-width: 10px;
    border-radius: 50px;
}

.nav-elem-login:hover {
    background: white;
}


</style>
