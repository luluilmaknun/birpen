<template>
  <div>
    <modal name="pop-box"
    :height="350"
    :pivotX="0.0" id = "center-div">
    <div class="modal-container">
        <h1 id="title-in-pop">Tambah Asisten</h1><br>
        <p id="desc-in-pop">Masukan user SSO Asisten</p><br>
        <input class="input" type="text" id="sso_username"/>
        <div class="modal-buttons">
        <button v-on:click="post_tambah_asisten" class="yellow-black-btn"
          id="tambah">TAMBAH</button>
        </div>
    </div>
    </modal>
    <button v-on:click="show" class="yellow-black-btn" id="tambah_asisten">
      TAMBAH ASISTEN</button>
  </div>
</template>

<script>

// import axios from 'axios';
export default {
  name: 'tambah-asisten',
  methods: {
    show() {
      this.$modal.show('pop-box');
    },
    // TO DO
    post_tambah_asisten() {
      this.$modal.hide('pop-box');
    //   const urlTarget = ''; // TO DO: API Tambah asisten
    //   axios({
    //     'method': 'POST',
    //     'url': urlTarget,
    //     'headers': {
    //       'content-type': 'application/x-www-form-urlencoded',
    //       'authorization': 'Token ' + sessionStorage.getItem('token'),
    //     }}).then((response) => {
    //     this.response = response.data;
    //     window.location.pathname=''; // TO DO: Pages daftar asisten
    //   }, (error) => {
    //     this.error=error;
    //   });
    },
  },
};
</script>

<style>
.modal-buttons button {
  margin-left: 20px;
  margin-right: 20px;
}

.modal-buttons {
  margin-top: 15px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.modal-container {
  margin: 70px 70px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.yellow-black-btn {
  color:black;
  background-color: #FFDD00;
  border-radius: 60.5px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 10pt;
  font-weight: bolder;
  border-style: none;
}

#title-in-pop {
  color:black;
  font-size: 35pt;
  font-weight: bold;
}

#desc-in-pop {
  color:black;
  font-size: 15pt;
  font-weight: lighter;
}

input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

</style>
