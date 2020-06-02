<template>
  <div id="pemesanan-tugas-akhir" class="page-container">
    <h2 class="title" style="color: black">
      Dokumen Kelengkapan<br>Sidang Akhir
    </h2>
    <br>
    <br>
    <form class="vue-form" @submit.prevent="submitData()">
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
            :key="jenis.nama">
            {{ jenis.nama }}
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
          Pembimbing Karya Akhir:
        </label>
        <input type="text" id="pembimbing" required=""
          v-model="pembimbing">
      </div>

      <div>
        <label class="label" for="pembimbing_pendamping">
          Pembimbing Karya<br>Akhir Pendamping:
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
import karyaAkhirApi from '@/services/karyaAkhirServices';

export default {
  name: 'PemesananTugasAkhir',
  data: function() {
    return {
      daftar_jenis_karya_akhir: [],
      peminatan_mahasiswa: '',
      sks_diperoleh: 0,
      pembimbing: '',
      pembimbing_pendamping: '',
      judul_karya_id: '',
      judul_karya_en: '',

      edit_flag: false,
      response: {},
      error_message: '',
      error_message_seen: false,
    };
  },
  created: function() {
    this.fetchData();
  },
  methods: {
    fetchData: function() {
      karyaAkhirApi.fetchJenisKaryaAkhir().then((d) => {
        this.response = d.data;

        this.setData(this.daftar_jenis_karya_akhir,
            this.response.jenis_karya_akhir);
      }).catch((e) => {
        this.error_message = 'Ada kesalahan pada database jenis karya akhir';
        this.error_message_seen = true;
      });

      karyaAkhirApi.getMahasiswaProfile().then((d) => {
        const data = d.data['mahasiswa'];

        this.nama = data['nama'];
        this.npm = data['npm'];
        this.program_studi = data['program_studi'];
      });

      karyaAkhirApi.readDataKaryaAkhir(localStorage.getItem('username'))
          .then((d) => {
            const data = d.data['data_karya_akhir'];
            this.edit_flag = true;

            this.peminatan_mahasiswa = data['peminatan_mahasiswa'];
            this.jenis_karya_akhir = data['jenis_karya_akhir'];
            this.sks_diperoleh = parseInt(data['sks_diperoleh']);
            this.pembimbing = data['pembimbing'];
            this.pembimbing_pendamping = data['pembimbing_pendamping'];
            this.judul_karya_id = data['judul_karya_id'];
            this.judul_karya_en = data['judul_karya_en'];
          }).catch((e) => {
            this.edit_flag = false;
          });
    },
    setData: function(target, source) {
      for (let i = 0; i < source.length; i++) {
        this.$set(target, i, source[i]);
      }
    },
    submitData: function() {
      const request = {};

      request['peminatan_mahasiswa'] = this.peminatan_mahasiswa;
      request['jenis_karya_akhir'] = this.jenis_karya_akhir;
      request['sks_diperoleh'] = this.sks_diperoleh;
      request['pembimbing'] = this.pembimbing;
      request['pembimbing_pendamping'] = this.pembimbing_pendamping;
      request['judul_karya_id'] = this.judul_karya_id;
      request['judul_karya_en'] = this.judul_karya_en;

      if (this.edit_flag) {
        this.editDataKaryaAkhir(request);
      } else {
        this.createDataKaryaAkhir(request);
      }
    },
    editDataKaryaAkhir: function(request) {
      karyaAkhirApi.editDataKaryaAkhir(request).then((d) => {
        this.$router.push('/surat/sidang/unduh/');
      }).catch((error) => {
        this.error_message = error.response.data.detail;
        this.error_message_seen = true;
      });
    },
    createDataKaryaAkhir: function(request) {
      karyaAkhirApi.createDataKaryaAkhir(request).then((d) => {
        this.$router.push('/surat/sidang/unduh/');
      }).catch((error) => {
        this.error_message = error.response.data.detail;
        this.error_message_seen = true;
      });
    },
  },
};
</script>

<style scoped>
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
