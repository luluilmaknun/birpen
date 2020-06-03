<template>
  <div>
    <h1>Mahasiswa Sidang Karya Akhir</h1>
    <div class="table-div">
      <!-- FILTER SECTION -->
      <div class="filter-div">
        <button v-on:click="performFilter(namaAngkatan, chosenStudi)"
        class="cari-button">
          Cari
        </button>
        <input placeholder="Tulis nama angkatan"
        class="filter-element" id="angkatan-input" v-model="namaAngkatan"/>
        <select class="filter-element" id="studi-choices" v-model="chosenStudi">
          <option selected disabled>-- Pilih Program Studi --</option>
          <option :value="''">Semua Program Studi</option>
          <option v-for="studi in programStudi"
          :key="studi.nama"
          :value="studi.nama">
            {{ studi.nama }}
          </option>
        </select>
      </div>
      <!-- UNFILTERED TABLE -->
      <table v-if="!isFilterLoaded">
        <tr>
          <th v-for="head in tableHead" :key="head" id="header">
            {{ head }}
          </th>
        </tr>
        <tr v-for="data in renderPagedList" :key="data.mahasiswa.nama">
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
            <DetailKaryaAkhir :username="data.mahasiswa.username"/>
          </td>
        </tr>
      </table>
      <!-- FILTERED TABLE -->
      <table v-else>
        <tr>
          <th v-for="head in tableHead" :key="head" id="header">
            {{ head }}
          </th>
        </tr>
        <tr v-for="data in renderPagedList" :key="data.mahasiswa.nama">
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
            <DetailKaryaAkhir :username="data.mahasiswa.username"/>
          </td>
        </tr>
      </table>
      <h2 class="errormsg"> {{ errormsg }} </h2>
    </div>
    <!-- PAGINATION -->
    <div class="pagination-section">
      <div class="button-box-2">
        <button class="pagination-button"
        id="first-page-button" v-show="showFirst" v-on:click="this.toFirstPage">
          &lt;&lt;
        </button>
      </div>
      <div class="button-box">
        <button class="pagination-button"
        id="prev-button" v-show="showPrev" v-on:click="this.decreamentPage">
          &lt;
        </button>
      </div>
      <div class="button-box">
        <p class="page-number">{{ pageNumber }}</p>
      </div>
      <div class="button-box">
        <button class="pagination-button"
        id="next-button" v-show="showNext" v-on:click="this.increamentPage">
          &gt;
        </button>
      </div>
      <div class="button-box-2">
        <button class="pagination-button"
        id="last-page-button" v-show="showLast" v-on:click="this.toLastPage">
          &gt;&gt;
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import apiSidangAkhir from '@/services/sidangKaryaAkhirServices.js';
import DetailKaryaAkhir from '@/components/detail-karya-akhir.vue';
export default {
  components: {
    DetailKaryaAkhir,
  },
  data: function() {
    return {
      showPrev: true,
      showNext: true,
      showFirst: true,
      showLast: true,
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
      pagedList: [],
      renderPagedList: [],
      pageNumber: 1,
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
        this.fetchPagination(this.karyaAkhir, this.pagedList);
        this.renderPagination(this.pageNumber, this.pagedList);
      });
    },
    performFilter: function(angkatan, prodi) {
      this.isFilterLoaded = true;
      this.filterKaryaAkhir(angkatan, prodi);
    },
    filterKaryaAkhir: function(angkatan, prodi) {
      this.pagedList = [];
      this.renderPagedList = [];
      this.pageNumber = 1;
      apiSidangAkhir.filterMahasiswa(angkatan, prodi).then((result) => {
        this.errormsg = '';
        if (result.data.detail != undefined) {
          this.errormsg = result.data.detail;
        }
        this.filteredKaryaAkhir = result.data.mahasiswa_karya_akhir;
        this.fetchPagination(this.filteredKaryaAkhir, this.pagedList);
        this.renderPagination(this.pageNumber, this.pagedList);
      });
    },
    fetchPagination: function(theList, pagedList) {
      const base = 7;
      let temp = [];
      let count = 0;
      for (let i = 0; i < theList.length; i++) {
        temp.push(theList[i]);
        count += 1;
        if (count == base) {
          count = 0;
          pagedList.push(temp);
          temp = [];
        } if (i == theList.length-1) {
          pagedList.push(temp);
          temp = [];
        }
      }
      if (pagedList[pagedList.length - 1] == 0) {
        const last = pagedList.length - 1;
        pagedList.splice(last, 1);
      }
    },
    renderPagination: function(pageNumber, pagedList) {
      this.checkPaginationButton(pageNumber, pagedList);
      const tempList = pagedList[pageNumber-1];
      this.renderPagedList = tempList;
    },
    increamentPage: function() {
      this.pageNumber++;
      this.renderPagination(this.pageNumber, this.pagedList);
    },
    decreamentPage: function() {
      this.pageNumber--;
      this.renderPagination(this.pageNumber, this.pagedList);
    },
    toFirstPage: function() {
      this.pageNumber = 1;
      this.renderPagination(this.pageNumber, this.pagedList);
    },
    toLastPage: function() {
      const last = this.pagedList.length;
      this.pageNumber = last;
      this.renderPagination(this.pageNumber, this.pagedList);
    },
    checkPaginationButton: function(pageNumber, pagedList) {
      if (pageNumber == 1 &&
      (pagedList.length == 1 || pagedList.length == 0)) {
        this.showPrev = false;
        this.showNext = false;
        this.showFirst = false;
        this.showLast = false;
      } else if (pageNumber == 1 && pagedList.length > 1) {
        // ujung kiri
        this.showPrev = false;
        this.showNext = true;
        this.showFirst = false;
        this.showLast = true;
      } else if (pageNumber == pagedList.length) {
        // ujung kanan
        this.showNext = false;
        this.showPrev = true;
        this.showFirst = true;
        this.showLast = false;
      } else {
        // tengah
        this.showNext = true;
        this.showPrev = true;
        this.showFirst = true;
        this.showLast = true;
      }
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
  margin-bottom: 20px;
  min-width: 100%;
}
.filter-div .filter-element {
  padding: 0;
  margin: 0;
  text-align: center;
  width: 200px;
  min-height: 20px;
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
/* Table styling */
.table-div {
  max-width: 1000px;
  min-width: 1000px;
  min-height: 600px;
  max-height: 600px;
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
  min-width: 100%;
}
th, td {
  padding-left: 1.5em;
  padding-right: 1.5em;
  padding-top: 1em;
  padding-bottom: 1em;
  word-wrap: break-word;
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
.pagination-section {
  margin-top: 30px;
  margin-bottom: 70px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.pagination-button {
  padding: 5px 10px;
  border-radius: 1000px;
  border-style: none;
  background: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: black;
  font-weight: bolder;
  font-size: 16pt;
  margin: 0;
}
.pagination-button:hover {
  background-color: #FFDD00;
}
#next-button {
  visibility: visible;
}
#prev-button {
  visibility: visible;
}
.button-box {
  width: 45px;
  height: 40px;
}
.button-box-2 {
  width: 75px;
  height: 40px;
}
.button-box, .button-box-2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.page-number {
  margin-left: 10px;
  margin-right: 10px;
}
.errormsg {
  color: red;
  margin-top: 30px;
  font-size: 16pt;
}
</style>
