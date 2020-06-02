<template>
  <div id="pemesanan-tugas-akhir" class="page-container">
    <h2 class="title" style="color: black">
      Dokumen Kelengkapan<br>Sidang Akhir
    </h2>
    <br>
    <br>
    <form class="vue-form" @submit.prevent="validateData()">
      <div>
        <label class="label" for="nama" style="display: inline">
          Nama:
        </label>
        <p id="nama" style="display: inline; margin: 0 0 20px 0">
          {{ nama }}
        </p>
      </div>

      <div>
        <label class="label" for="npm" style="display: inline">
          NPM:
        </label>
        <p id="npm" style="display: inline; margin: 0 0 20px 0">
          {{ npm }}
        </p>
      </div>

      <div>
        <label class="label" for="program_studi" style="display: inline">
          Program Studi:
        </label>
        <p id="program_studi" style="display: inline; margin: 0 0 20px 0">
          {{ program_studi }}
        </p>
      </div>

      <div>
        <label class="label" for="peminatan_mahasiswa">
          Peminatan:
        </label>
        <input type="text" id="peminatan_mahasiswa" required=""
          v-model="peminatan_mahasiswa">
      </div>

      <div>
        <label class="label" for="jenis_karya_akhir">
          Jenis Karya Akhir:
        </label>
        <select id="jenis_karya_akhir" v-model="jenis_karya_akhir">
          <option v-for="jenis in daftar_jenis_karya_akhir"
            :key="jenis">
            {{ jenis }}
          </option>
        </select>
      </div>

      <div>
        <label class="label" for="sks_diperoleh">
          Jumlah SKS diperoleh:
        </label>
        <input type="number" id="sks_diperoleh" required=""
          v-model="sks_diperoleh">
      </div>

      <div>
        <label class="label" for="pembimbing">
          Jumlah SKS diperoleh:
        </label>
        <input type="text" id="pembimbing" required=""
          v-model="pembimbing">
      </div>

      <div>
        <label class="label" for="pembimbing_pendamping">
          Jumlah SKS diperoleh:
        </label>
        <input type="text" id="pembimbing_pendamping" required=""
          v-model="pembimbing_pendamping">
      </div>

      <div class="textarea-wrapper">
        <label class="label" for="judul_karya_id">
          Judul Karya Akhir dalam Bahasa Indonesia:
        </label>
        <textarea type="text" id="judul_karya_id"
          v-model="judul_karya_id" />
      </div>

      <div class="textarea-wrapper">
        <label class="label" for="judul_karya_en">
          Judul Karya Akhir dalam Bahasa Inggris:
        </label>
        <textarea type="text" id="judul_karya_en"
          v-model="judul_karya_en" />
      </div>

      <br>
      <span style="text-align:center;color:red"
        v-if="message_seen">
        {{ message }}
      </span>
      <button type="submit">
        Simpan
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
#pemesanan-tugas-akhir {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3%;
}
h2.title {
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: 45px;
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
  font-size: 23px;
  line-height: 37px;
  width: 50%;
  margin: auto;
}
form.vue-form p{
  font-size: 23px;
  width: 50%;
  font-weight: bold;
}
form.vue-form input, form.vue-form select, form.vue-form textarea {
  background: #FFFFFF;
  border-radius: 11px;
  width: 50%;
  font-size: 23px;
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
  font-size: 23px;
  margin: 30px 0;
  line-height: 37px;
  align-self: center;
  text-align: center;
  cursor: pointer;
}
form.vue-form .textarea-wrapper {
  display: flex;
  flex-direction: column;
}
form.vue-form .textarea-wrapper textarea {
  width: 100%;
  padding: 6px;
}
form.vue-form .textarea-wrapper label {
  width: 100%;
  margin: 15px 0;
}
@media only screen and (max-width: 1000px) {
  form.vue-form {
    width: 75%;
  }
}
</style>
