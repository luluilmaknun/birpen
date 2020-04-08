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
            window.location.pathname='/pengumuman';
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
  font-weight: bolder;
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
}
.nav-elem:hover {
  background-color: white;
  color: black;
}
#hapus-btn {
  color:white;
  background-color: #E63946;
  border-radius: 100px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
}
#blue-btn {
  color:white;
  background-color: #7584D1;
  border-radius: 100px;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 20pt;
}

#center-div {
  display:flex;
  justify-content: center;
  align-items: center;
}

#login-button:hover {
  background-color: white;
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
