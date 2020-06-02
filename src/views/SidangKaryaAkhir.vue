<template>
  <div>
    <h1>Mahasiswa Sidang Karya Akhir</h1>
    <div class="main-container">
      <div class="filter-div">
        <button v-on:click="performFilter(namaAngkatan, chosenStudi)"
        class="cari-button">
          Cari
        </button>
        <input placeholder="Tulis nama angkatan"
        class="filter-element" id="angkatan-input" v-model="namaAngkatan"/>
        <select class="filter-element" id="studi-choices" v-model="chosenStudi">
          <option :value="''" hidden>Pilih Program Studi</option>
          <option v-for="studi in programStudi"
          :key="studi.nama"
          :value="studi.nama">
            {{ studi.nama }}
          </option>
        </select>
      </div>
      <!-- TABLE SECTION -->
      <div v-if="!isFilterLoaded" class="table-div">
        <table>
          <tr>
            <th v-for="head in tableHead" :key="head" id="header">
              {{ head }}
            </th>
          </tr>
          <tr v-for="data in karyaAkhir" :key="data.mahasiswa.nama">
            <td id="mahasiswa">
              {{ data.mahasiswa.nama }}
            </td>
            <td id="npm">
              {{ data.mahasiswa.npm }}
            </td>
            <td id="program_studi ">
              {{ data.mahasiswa.program_studi }}
            </td>
            <td id="angkatan">
              {{ data.mahasiswa.angkatan }}
            </td>
            <td id="detail-col">
              <button class="detail-button">
                Detail
              </button>
            </td>
          </tr>
        </table>
      </div>
      <!-- FILTERED TABLE -->
      <div v-else class="table-div">
        <table>
          <tr>
            <th v-for="head in tableHead" :key="head" id="header">
              {{ head }}
            </th>
          </tr>
          <tr v-for="data in filteredKaryaAkhir" :key="data.mahasiswa.nama">
            <td id="mahasiswa">
              {{ data.mahasiswa.nama }}
            </td>
            <td id="npm">
              {{ data.mahasiswa.npm }}
            </td>
            <td id="program_studi ">
              {{ data.mahasiswa.program_studi }}
            </td>
            <td id="angkatan">
              {{ data.mahasiswa.angkatan }}
            </td>
            <td id="detail-col">
              <button class="detail-button">
                Detail
              </button>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import apiSidangAkhir from '@/services/sidangKaryaAkhirServices.js';
export default {
  data: function() {
    return {
      namaAngkatan: '',
      chosenStudi: '',
      tableHead: [
        'Nama', 'NPM', 'Program Studi', 'Angkatan', 'Aksi',
      ],
      programStudi: [],
      karyaAkhir: [],
      filteredKaryaAkhir: [],
      errormsg: '',
      isFilterLoaded: false,
    };
  },
  created: function() {
    this.fetchProgramStudi();
    this.fetchKaryaAkhir();
  },
  methods: {
    fetchProgramStudi: function() {
      apiSidangAkhir.getProgramStudi().then((result) => {
        this.programStudi = result.data.program_studi;
      });
    },
    fetchKaryaAkhir: function() {
      apiSidangAkhir.getKaryaAkhir().then((result) => {
        this.karyaAkhir = result.data.mahasiswa_karya_akhir;
      });
    },
    performFilter: function(angkatan, prodi) {
      this.isFilterLoaded = true;
      this.filterKaryaAkhir(angkatan, prodi);
    },
    filterKaryaAkhir: function(angkatan, prodi) {
      apiSidangAkhir.filterMahasiswa(angkatan, prodi).then((result) => {
        this.filteredKaryaAkhir = result.data.mahasiswa_karya_akhir;
      });
    },
  },
};
</script>

<style scoped>
.filter-div {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  margin-top: 20px;
}
.filter-div .filter-element {
  text-align: center;
  width: 200px;
  background: none;
  border-style: solid;
  border-width: 2px;
  border-color: black;
  background-color: white;
  border-radius: 10px;
  padding: 10px 10px;
  margin: 0;
  margin-left: 10px;
  margin-right: 10px;
}
.detail-button {
  background: none;
  border-style: solid;
  border-width: 2px;
  border-radius: 100px;
  color: white;
  background-color: #5386E8;
  border-color: #5386E8;
  font-weight: bolder;
  padding: 5px;
}
.detail-button:hover {
  background-color: white;
  color: #5386E8;
}
/* Table styling */
.table-div {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}
.table-div table {
  border-radius: 1em;
  text-align: center;
  overflow: hidden;
  border-collapse: collapse;
  width: 100%;
}
th, td {
  padding-left: 1.5em;
  padding-right: 1.5em;
  padding-top: 1em;
  padding-bottom: 1em;
}
th {
  background-color: #2D3033;
  font-weight: bolder;
  color: white;
  font-size: 15pt;
}
tr:nth-child(odd) {
  background-color: #D3D3D3;
}
.cari-button {
  background: none;
  border-style: solid;
  background-color: #FFDD00;
  border-color: #FFDD00;
  border-radius: 1000px;
  color: black;
  font-weight: bolder;
  padding: 10px 15px;
  margin: 0;
  margin-left: 20px;
}
.cari-button:hover {
  background-color: white;
}
</style>
