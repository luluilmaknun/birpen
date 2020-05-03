<template>
  <div id="create-announcement" class="page-container">
    <h2 v-if="edit" class="title" style="color: black">Edit Pengumuman</h2>
    <h2 v-else class="title" style="color: black">Buat Pengumuman</h2>
    <br>
    <br>
    <form class="vue-form" @submit.prevent="validateData()">
      <div>
        <label class="label" for="pembuat" style="display: inline">
          Dibuat oleh:
        </label>
        <p id="pembuat" style="display: inline; margin: 0 0 20px 0">
          {{ pembuat }}
        </p>
      </div>

      <div>
        <label class="label" for="tanggal_kelas">
          Tanggal Kelas:
        </label>
        <input type="date" id="tanggal_kelas"
          required="" v-model="tanggal_kelas">
      </div>

      <div>
        <label class="label" for="nama_mata_kuliah">
          Mata Kuliah:
        </label>
        <select id="nama_mata_kuliah" v-model="nama_mata_kuliah">
          <option v-for="mata_kuliah in daftar_mata_kuliah" :key="mata_kuliah">
            {{ mata_kuliah }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="jenis_pengumuman">
          Jenis Pengumuman:
        </label>
        <select id="jenis_pengumuman" v-model="jenis_pengumuman">
          <option v-for="jenis in daftar_jenis_pengumuman" :key="jenis">
            {{ jenis }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="nama_dosen">
          Dosen:
        </label>
        <input type="text" id="nama_dosen" required="" v-model="nama_dosen">
      </div>

      <div v-if="jenis_pengumuman.toLowerCase() == 'asistensi'">
        <label class="label" for="nama_asisten">
          Asisten:
        </label>
        <input type="text" id="nama_asisten" required="" v-model="nama_asisten">
      </div>

      <div>
        <label class="label" for="nama_ruang">
          Ruang:
        </label>
        <select id="nama_ruang" v-model="nama_ruang">
          <option v-for="ruang in daftar_nama_ruang" :key="ruang">
            {{ ruang }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="nama_sesi">
          Sesi:
        </label>
        <select id="nama_sesi" v-model="nama_sesi">
          <option v-for="sesi in daftar_nama_sesi" :key="sesi">
            {{ sesi }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="nama_status_pengumuman">
          Status:
        </label>
        <select id="nama_status_pengumuman" v-model="nama_status_pengumuman">
          <option v-for="status in daftar_nama_status_pengumuman" :key="status">
            {{ status }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="komentar">
          Komentar:
        </label>
        <textarea type="text" id="komentar" v-model="komentar" />
      </div>
      <br>
      <span style="text-align:center;color:red"
        v-if="message_seen">
        {{ message }}
      </span>
      <button type="submit">
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import dropdownApi from '@/services/dropdownDataServices';
import announcementApi from '@/services/announcementServices';

export default {
  name: 'CreateAnnouncement',
  props: {
    edit: Boolean,
    pk: String,
  },
  data: function() {
    return {
      role: localStorage.getItem('role'),
      is_admin: localStorage.getItem('is_admin'),
      is_asdos: localStorage.getItem('is_asdos'),
      pembuat: localStorage.getItem('username'),
      jenis_pengumuman: '',
      tanggal_kelas: '',
      nama_mata_kuliah: '',
      nama_dosen: '',
      nama_asisten: '',
      nama_sesi: '',
      nama_ruang: '',
      nama_status_pengumuman: '',
      komentar: '',
      daftar_mata_kuliah: [],
      daftar_jenis_pengumuman: [],
      daftar_nama_ruang: [],
      daftar_nama_sesi: [],
      daftar_nama_status_pengumuman: [],

      response: {},
      error_message: '',
      error_message_seen: false,
    };
  },
  created: function() {
    this.fetchData();

    if (this.edit) {
      this.getAnnouncementData(this.pk);
    }
  },
  methods: {
    fetchData: function() {
      dropdownApi.fetch().then((d) => {
        this.response = d.data;

        this.setData(this.daftar_jenis_pengumuman,
            this.response.jenis_pengumuman);
        this.setData(this.daftar_mata_kuliah,
            this.response.mata_kuliah);
        this.setData(this.daftar_nama_ruang,
            this.response.ruang);
        this.setData(this.daftar_nama_sesi,
            this.response.sesi);
        this.setData(this.daftar_nama_status_pengumuman,
            this.response.status_pengumuman);
      });
    },
    setData: function(target, source) {
      for (let i = 0; i < source.length; i++) {
        this.$set(target, i, source[i]);
      }
    },
    getAnnouncementData: function(pk) {
      announcementApi.getAnnouncement(pk).then((d) => {
        const data = d.data.pengumuman;

        if (this.is_admin == 'false' && this.pembuat != data['pembuat']) {
          this.$router.push('/pengumuman/');
        }

        this.pembuat = data['pembuat'];
        this.nama_mata_kuliah = data['nama_mata_kuliah'];
        this.jenis_pengumuman = data['jenis_pengumuman'];
        this.komentar = data['komentar'];
        this.nama_dosen = data['nama_dosen'];
        this.nama_ruang = data['nama_ruang'];
        this.tanggal_kelas = data['tanggal_kelas'];
        this.nama_sesi = data['nama_sesi'];
        this.nama_status_pengumuman = data['nama_status_pengumuman'];

        if (this.jenis_pengumuman == 'Asistensi') {
          this.nama_asisten = data['nama_asisten'];
        }
      });
    },
    validateData: function() {
      const request = {};

      const jamKelas = this.nama_sesi.match(/[0-2][0-9].[0-9][0-9]/)[0];
      const jamMulai = jamKelas.replace('.', ':');
      const timeKelas = new Date(this.tanggal_kelas + ' ' + jamMulai);
      const timeNow = new Date();
      if (timeKelas > timeNow) {
        request['tanggal_kelas'] = this.tanggal_kelas;
        request['jenis_pengumuman'] = this.jenis_pengumuman;
        request['nama_mata_kuliah'] = this.nama_mata_kuliah;
        request['nama_dosen'] = this.nama_dosen;
        request['nama_asisten'] = this.nama_asisten;
        request['nama_sesi'] = this.nama_sesi;
        request['nama_ruang'] = this.nama_ruang;
        request['nama_status_pengumuman'] = this.nama_status_pengumuman;
        request['komentar'] = this.komentar;

        if (this.edit) {
          this.editAnnouncement(this.pk, request);
        } else {
          this.createAnnouncement(request);
        }
      } else {
        this.error_message = 'Kelas sudah lampau';
        this.error_message_seen = true;
      }
    },
    editAnnouncement: function(pk, request) {
      announcementApi.editAnnouncement(pk, request).then((d) => {
        this.$router.push('/pengumuman/');
      }).catch((error) => {
        this.error_message = error.response.data.detail;
        this.error_message_seen = true;
      });
    },
    createAnnouncement: function(request) {
      announcementApi.createAnnouncement(request).then((d) => {
        this.$router.push('/pengumuman/');
      }).catch((error) => {
        this.error_message = error.response.data.detail;
        this.error_message_seen = true;
      });
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
}
.w-100 {
  width: 100%;
}
.w-50 {
  width: 50%;
}
#create-announcement {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3%;
}
h2.title {
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: 60px;
  line-height: 73px;
  text-align: center;
}
form.vue-form {
  background: #2D3033;
  border-radius: 18px;
  padding: 5%;
  width: 800px;
  display: flex;
  flex-direction: column;
  color: white;
}
form.vue-form label {
  font-size: 30px;
  line-height: 37px;
  width: 50%;
}
form.vue-form p{
  font-size: 30px;
  width: 50%;
  font-weight: bold;
}
form.vue-form input, form.vue-form select, form.vue-form textarea {
  background: #FFFFFF;
  border-radius: 11px;
  width: 50%;
  font-size: 30px;
  font-family: 'Montserrat', sans-serif;
  border: 0;
  box-sizing: border-box;
  text-align: left;
  padding-left: 20px;
}
form.vue-form input, form.vue-form select {
  height: 55px;
}
form.vue-form textarea {
  height: 120px;
}
form.vue-form div {
  margin: 15px 0;
  display: flex;
}
form.vue-form button {
  width: 244px;
  background: #FFDD00;
  border: 0;
  border-radius: 46.5px;
  font-family: 'Montserrat', sans-serif;
  font-style: normal;
  font-weight: bold;
  padding: 10px;
  font-size: 30px;
  margin: 30px 0;
  line-height: 37px;
  align-self: center;
  text-align: center;
  cursor: pointer;
}
@media only screen and (max-width: 1000px) {
  form.vue-form {
    width: 75%;
  }
}
</style>
