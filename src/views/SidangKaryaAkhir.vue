<template>
  <div>
    <h1>Mahasiswa Sidang Karya Akhir</h1>
    <div class="main-container">
      <div class="filter-div">
        <select class="filter-element" id="studi-choices" v-model="chosenStudi">
          <option :value="''" hidden>Pilih Program Studi</option>
          <option v-for="studi in programStudiDummy"
          :key="studi.pk"
          :value="studi.nama">
            {{ studi.nama }}
          </option>
        </select>
        <input placeholder="Tulis nama angkatan"
        class="filter-element" id="angkatan-input" v-model="angkatan"/>
      </div>
      <!-- TABLE SECTION -->
      <div class="table-div">
        <table>
        <tr>
          <th v-for="head in tableHead" :key="head" id="header">
            {{ head }}
          </th>
        </tr>
        <tr v-for="data in karyaAkhirDummy" :key="data.pk">
          <td id="mahasiswa">
            {{ data.mahasiswa }}
          </td>
          <td id="npm">
            {{ data.npm }}
          </td>
          <td id="peminatan_mahasiswa ">
            {{ data.peminatan_mahasiswa }}
          </td>
          <td id="angkatan">
            {{ data.angkatan }}
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
      angkatan: '',
      chosenStudi: '',
      tableHead: [
        'Nama', 'NPM', 'Program Studi', 'Angkatan', 'Aksi',
      ],
      karyaAkhirDummy: [
        {
          pk: 1,
          mahasiswa: 'Yusuf Tri Ardho',
          npm: '1706023024',
          angkatan: '2017',
          peminatan_mahasiswa: "Akuntansi Terapan",
          jenis_karya_akhir: 1,
          sks_diperoleh: 144,
          pembimbing: "Lulu Ilmaknun S.Ak.",
          pembimbing_pendamping: "Annida Safira S.Ak.",
          judul_karya_id: "Akuntansi dalam bisnis",
          judul_karya_en: "Accounting in business",
        },
        {
          pk: 2,
          mahasiswa: 'Napis',
          npm: '1706075022',
          angkatan: '2016',
          peminatan_mahasiswa: "Akuntansi Virtual",
          jenis_karya_akhir: 1,
          sks_diperoleh: 144,
          pembimbing: "Bulan",
          pembimbing_pendamping: "-",
          judul_karya_id: "Akuntansi dalam bisnis",
          judul_karya_en: "Accounting with VR",
        },
        {
          pk: 3,
          mahasiswa: 'Azhar',
          npm: '1706024864',
          angkatan: '2019',
          peminatan_mahasiswa: "Ilmu Ekonomi Terapan",
          jenis_karya_akhir: 2,
          sks_diperoleh: 141,
          pembimbing: "Bebes",
          pembimbing_pendamping: "-",
          judul_karya_id: "Ekonomi dalam bisnis",
          judul_karya_en: "Ekonomi in social life",
        },
      ],
      programStudiDummy: [
        {
          pk: 1,
          nama: 'Manajemen'
        },
        {
          pk: 2,
          nama: 'Akuntansi'
        },
        {
          pk: 3,
          nama: 'Bisnis Islam'
        },
        {
          pk: 4,
          nama: 'Ilmu Ekonomi Islam'
        },
      ],
      programStudiResponse: {},
    };
  },
  created: function() {
    this.fetchProgramStudi();
  },
  methods: {
    fetchProgramStudi: function() {
      apiSidangAkhir.getProgramStudi().then((result) => {
        this.programStudiResponse = result.data;
      })
    }
  },
}
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
</style>