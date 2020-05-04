<template>
  <div id="dokumen-akademik" class="page-container">
    <h2 class="title">Pemesanan Surat <br> Akademik </h2>
    <br>

    <div class="profile-container">
      <div class="input-row">
        <label>Nama: </label>
        <input v-if="isAlumni" class="profile-input" v-model="nama_pemesan">
        <span v-else class="">Lulu Ilmaknun Qurotaini</span>
      </div>

      <div class="input-row">
        <label>NPM: </label>
        <input v-if="isAlumni" class="profile-input" v-model="npm_pemesan">
        <span v-else class="">1706979341</span>
      </div>
    </div>

    <!-- TABLE SECTION -->
    <table>
      <tr class="table-header">
        <th class="table-header-item" v-for="head in tableHead" :key="head"
          :id="head[0]">
          {{ head[1] }}
        </th>
      </tr>

      <tr v-for="(item, id) in surat_akademik" :id="id+1" :key="item">
        <td class="no">
          {{ id+1 }}
        </td>
        <td class="jenis_dokumen">
          {{ item.jenis_dokumen }}
        </td>
        <td class="harga_satuan">
          Rp.
          <span v-if="isAlumni">{{ item.harga_alumni }}</span>
          <span v-else>{{ item.harga_mahasiswa }}</span>
        </td>
        <td class="jumlah">
          <div class="button-count-container">
            <button class="btn-count" @click="update('increment', id)">
              +
            </button>
            <input type="number" :ref="id+1" class="jumlah_surat" value=0 >
            <button class="btn-count" @click="update('decrement', id)">
              -
            </button>
          </div>
        </td>
      </tr>
    </table>

    <div class="button-container pemesanan">
      <button @click="showModal('ringkasan')">Pesan</button>
      <button @click="goToPage('surat')">Kembali</button>
    </div>

    <modal name="ringkasan" height="auto" :pivotX="0.0">
      <div class="button-container ringkasan">
        <button class="btn btn-red" @click="closeModal('ringkasan')">
          Batal
        </button>

        <button class="btn btn-grn" @click="validateData">
          Pesan
        </button>
      </div>
    </modal>
  </div>
</template>

<script>
export default {
  name: 'DokumenAkademik',
  data: function() {
    return {
      // isAlumni: localStorage['role'] == 'alumni',
      isAlumni: true,
      tableHead: [
        ['no', 'No'],
        ['jenis_dokumen', 'Jenis Dokumen'],
        ['harga_satuan', 'Harga Satuan'],
        ['jumlah', 'Jumlah'],
      ],
      nama_pemesan: '',
      npm_pemesan: '',
      surat_akademik: [
        {
          'jenis_dokumen': 'Surat Keterangan Mahasiswa',
          'harga_mahasiswa': 0,
          'harga_alumni': 10000,
        },
        {
          'jenis_dokumen': 'Surat Keterangan Tidak Lulus',
          'harga_mahasiswa': 50000,
          'harga_alumni': 50000,
        },
        {
          'jenis_dokumen': 'Surat Mencintai dirinya',
          'harga_mahasiswa': 0,
          'harga_alumni': 10000,
        },
        {
          'jenis_dokumen': 'Surat-suratan sama doi',
          'harga_mahasiswa': 0,
          'harga_alumni': 0,
        },
      ],
    };
  },
  created() {
    this.fetchLetterList();
  },
  methods: {
    fetchLetterList() {
      // TODO
    },
    update(type, id) {
      const inputId = id + 1;
      const input = this.$refs[inputId][0];

      if (type == 'increment') {
        input.value = parseInt(input.value) + 1;
      } else if (type == 'decrement') {
        input.value = parseInt(input.value) - 1;
      }
    },
    showModal(name) {
      this.$modal.show(name);
    },
    closeModal(name) {
      this.$modal.hide(name);
    },
    goToPage(path) {
      this.$router.push({name: path});
    },
    validateData() {
      // TODO
    },
    requestLetter() {
      // TODO
    },
  },
};
</script>

<style scoped>
#dokumen-akademik.page-container {
  padding: 3% 8%;
}
#dokumen-akademik .title {
  font-weight: 700;
  font-size: 40px;
  line-height: 45px;
  text-align: center;
  color: #000;
}
.profile-container {
  padding: 30px;
  margin-left: 10px;
  font-size: 18px;
}
.profile-container .input-row {
  margin: 20px;
}
.profile-container .input-row label {
  width: 100px;
  display: inline-block;
}
.profile-container .input-row span {
  font-weight: 700;
  display: inline-block;
}
.profile-container input {
  height: 25px;
  border-radius: 7px;
  border: 1px solid black;
  width: 250px;
  padding: 6px;
  font-weight: 700;
}
</style>
