<template>
  <div>
    <modal v-bind:name=this.alumni_username
    @before-open="error_message=''"
    height="auto"
    :pivotX="0.0">
    <div class="modal-container">
        <div class="warning-msg">
          <h1 id="desc-modal">Apakah anda yakin akan
            <d v-if="is_blocked">membatalkan blokir pada</d>
            <d v-else>memblokir</d>
          <b>&nbsp;{{ this.alumni_username }}</b>
          sebagai alumni?</h1>
          <p id="error-message">{{ error_message }}</p>
        </div>
        <div class="modal-buttons">
          <div v-if="is_blocked">
            <button @click="toggle_alumni" class="unblock-button"
              id="block-conf">Batalkan blokir</button>
          </div><div v-else>
            <button @click="toggle_alumni" class="block-button"
              id="unblock-conf">Blokir</button>
          </div>
        <button @click="close_modal" class="tidak-btn"
          id="tidak-btn">Tidak</button>
        </div>
    </div>
    </modal>

    <div v-if="is_blocked">
      <button class="block-button" id="unblock-btn"
      @click="open_modal">Batalkan blokir</button>
    </div><div v-else>
      <button class="block-button" id="block-btn"
      @click="open_modal">Blokir</button>
    </div>

  </div>
</template>

<script>
import alumniServices from '@/services/alumniServices';

export default {
  name: 'toggle-block-alumni',
  data: function() {
    return {
      'error_message': '',
    };
  },
  props: {
    alumni_username: String,
    is_blocked: Boolean,
  },
  methods: {
    open_modal: function() {
      this.$modal.show(this.alumni_username);
    },
    close_modal: function() {
      this.$modal.hide(this.alumni_username);
    },
    toggle_alumni: function() {
      alumniServices.toggleBlockAlumni(this.alumni_username, {
        is_blocked: !this.is_blocked,
      }).then((result) => {
        this.$router.go();
      }).catch((error) => {
        this.error_message = error.response.data.detail;
      });
    },
  },
};
</script>

<style scoped>

.modal-buttons button {
  margin-left: 10px;
  margin-right: 10px;
}

.modal-buttons {
  margin-top: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.modal-container {
  margin: 30px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#desc-modal {
  color:black;
  font-size: 13pt;
  font-weight: 500;
  text-align: center;
}

.block-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: #E63946;
  background-color: #E63946;
  border-radius: 1000px;
}

.block-button:hover {
  background-color: white;
  color: #E63946;
}

.unblock-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: #206bdd;
  background-color: #206bdd;
  border-radius: 1000px;
}

.unblock-button:hover {
  background-color: white;
  color: #206bdd;
}

.tidak-btn {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: black;
  background-color: black;
  border-radius: 1000px;
}

.tidak-btn:hover {
  background-color: white;
  color: black;
}

#error-message {
  color: red;
  font-size: 10pt;
  font-weight: bold;
  margin: 10px 10px;
  text-align: center;
}
</style>
