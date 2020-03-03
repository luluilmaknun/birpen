<template>
    <div class="nav-container">

        <div class="nav-elem-container-left">
            <h2>
                Biro Pendidikan FEB
            </h2>
        </div>

        <div class="nav-elem-container-right">
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
</template>

<script>
export default {
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
    flex-wrap: wrap;
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

#login-button {
    color:black;
    background-color: yellow;
    border-radius: 100px;
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 5px;
    padding-bottom: 5px;
    font-size: 20pt;
}

#login-button:hover {
    background-color: white;
}

.nav-elem-login:hover {
    background: white;
}


</style>
