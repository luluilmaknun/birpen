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
    <table class="table-div">
      <tr class="table-header">
        <th class="table-header-item" v-for="head in tableHead" :key="head"
          :class="head[0]">
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
          <span v-if="isAlumni">{{ item.harga_alumni }}</span>
          <span v-else>{{ item.harga_mahasiswa }}</span>
        </td>
        <td class="jumlah">
          <div class="button-count-container">
            <button class="btn-count decrement"
              @click="update('decrement', id)">
              -
            </button>
            <input type="number" :ref="id+1"
              class="jumlah_surat" value=0 min=0 >
            <button class="btn-count increment"
              @click="update('increment', id)">
              +
            </button>
          </div>
        </td>
      </tr>
    </table>

    <br>
    <br>
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
      isAlumni: localStorage['role'] == 'alumni',
      // isAlumni: true,
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
      const currValue = parseInt(input.value);

      if (type == 'increment') {
        input.value = currValue + 1;
      } else if (type == 'decrement') {
        // Check for minimum value zero
        if (currValue == 0) {
          input.value = 0;
        } else {
          input.value = currValue - 1;
        }
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
table.table-div {
  width: 100%;
  border: 1.5px solid black;
  border-radius: 1em;
  border-spacing: 0;
}
th:first-of-type {
  border-top-left-radius: 10px;
}
th:last-of-type {
  border-top-right-radius: 10px;
}
th {
  background-color: black;
  padding: 13px;
  color: white;
  font-weight: 700;
}
td {
  padding: 13px;
  border-bottom: .5px solid black;
}
tr:last-of-type td {
  border-bottom: 0;
}
th.no, td.no {
  width: 5%;
  text-align: center;
}
th.jenis_dokumen, td.jenis_dokumen {
  width: 65%;
  text-align: left;
}
th.harga_satuan, td.harga_satuan {
  width: 15%;
  text-align: center;
}
th.jumlah, td.jumlah {
  width: 15%;
  min-width: 85px;
  text-align: center;
}
button.btn-count {
  border: 0;
  background-color: #FFDD00;
  color: black;
  cursor: pointer;
  padding: 7px 10px;
}
button.btn-count.increment {
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}
button.btn-count.decrement {
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}
input.jumlah_surat {
  width: 40px;
  border: 0;
  text-align: center;
  padding: 0;
}
input[type='number'] {
    -moz-appearance:textfield;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}
.button-container.pemesanan {
  margin-right: 50px;
}
.button-container.pemesanan button {
  border: 0;
  border-radius: 30px;
  background-color: #D8DADB;
  color: black;
  font-weight: 700;
  cursor: pointer;
  margin: 20px;
  padding: 15px;
  min-width: 150px;
}
.button-container.ringkasan {
  margin: auto;
  padding: 5%;
  text-align: center;
}
.button-container.ringkasan .btn {
  font-size: 23px;
  font-weight: bolder;
  border: 0px;
  padding: 8px 30px;
  width: 135px;
  border-radius: 34.5px;
  margin: 15px;
}
.button-container.ringkasan .btn-grn {
  background: #3C8F2F;
  color: white;
}
.button-container.ringkasan .btn-red {
  background: #E63946;
  color: white;
}
</style>
