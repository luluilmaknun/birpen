<template>
  <div>
    <modal name="hello-world"
    :pivotX="0.0" id = "center-div">
        <div class="modal-container">
          Apakah anda yakin?
          <div class="modal-buttons">
            <button v-on:click="deletePengumuman" id='blue-btn'>Ya</button>
            <button v-on:click="hide" id="hapus-btn">Tidak</button>
          </div>
        </div>
    </modal>
    <button v-on:click="show" id="hapus-btn" >Hapus</button>

  </div>
</template>

<script>

import axios from 'axios';
export default {
  name: 'delete',
  methods: {
    // bikin fungsi
    show() {
      this.$modal.show('hello-world');
    },
    hide() {
      this.$modal.hide('hello-world');
    },
    deletePengumuman() {
      const urlTarget = '/api/pengumuman/'+
      document.getElementById('pk').innerText+'/delete/';
      axios({'method': 'DELETE', 'url': urlTarget,
        'headers':
      {
        'content-type': 'application/x-www-form-urlencoded',
        'authorization': 'Bearer ' + localStorage.getItem('token'),
      }}).then(
          (response) => {
            this.response = response.data;
            window.location.pathname='/pengumuman/';
          },
          (error) => {
            this.error=error;
          });
    },
  },
};
</script>

<style>
.modal-buttons button {
  margin-left: 20px;
  margin-right: 20px;
  font-weight: bolder;
  border-style: none;
}
.modal-buttons {
  margin-top: 40px;
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
h2 {
  font-size: 26pt;
  color: white;
}
#hapus-btn {
  color:white;
  background-color: #E63946;
  border-color: #E63946;
  border-radius: 100px;
  border-style: solid;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
  font-weight: bolder;
}
#hapus-btn:hover {
  color: #E63946;
  background-color: white;
}
#blue-btn {
  color:white;
  background-color: #7584D1;
  border-color: #7584D1;
  border-radius: 100px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
  border-style: solid;
}
#blue-btn:hover {
  color: #7584D1;
  background-color: white;
}
#center-div {
  display:flex;
  justify-content: center;
  align-items: center;
}
</style>
