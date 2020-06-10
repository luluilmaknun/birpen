<template>
  <div v-if="isFetchAsdos">
    <img src="@/assets/icons/loader.svg"/>
  </div>
  <div v-else>

    <h1 class="title-asdos">
      Daftar Asisten
    </h1>

    <div class="create-asisten-div">
      <CreateAsisten/>
    </div>
    <!-- TABLE SECTION -->
    <div class="table-div">
      <table aria-hidden="true">
        <tr>
          <th id="table-header" class="head-table"
            v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="asisten in renderPagedList" :key="asisten.username">
          <td id="username">
            {{ asisten.username }}
          </td>
          <td>
            <DeleteAsisten :deleted_asisten_username="asisten.username"/>
          </td>
        </tr>
      </table>
    </div>
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
        <p class="page-number">{{ pageNumber }} of {{ pagedList.length }}</p>
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
import asistenServices from '@/services/asistenServices';
import CreateAsisten from '@/components/tambah-asisten';
import DeleteAsisten from '@/components/delete-asisten';

export default {
  name: 'AsdosPage',
  data: function() {
    return {
      tableHead: [
        'Username', 'Aksi',
      ],
      listAsdos: [
        {
          'pk': 0,
          'username': 'athallah.annafis',
        },
        {
          'pk': 1,
          'username': 'ichlassul.affan',
        },
        {
          'pk': 2,
          'username': 'ahmad.fauzan',
        },
        {
          'pk': 3,
          'username': 'asdos',
        },
      ],
      response: {},
      listAsisten: [],
      isFetchAsdos: false,
      showPrev: true,
      showNext: true,
      showFirst: true,
      showLast: true,
      pagedList: [],
      renderPagedList: [],
      pageNumber: 1,
    };
  },
  created: function() {
    this.fetchAsdos();
  },
  methods: {
    fetchAsdos: function() {
      this.isFetchAsdos = true;
      asistenServices.getAsisten().then((d) => {
        this.response = d.data;
        for (let i = 0; i < this.response.asisten_dosen.length; i++) {
          this.$set(this.listAsisten, i, this.response.asisten_dosen[i]);
        }
        this.fetchPagination(this.listAsisten, this.pagedList);
        this.renderPagination(this.pageNumber, this.pagedList);
        this.isFetchAsdos = false;
      });
    },
    fetchPagination: function(theList, pagedList) {
      const base = 5;
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
  components: {
    CreateAsisten, DeleteAsisten,
  },
};
</script>

<style scoped>
.title-asdos {
  margin-top: 50px;
  margin-bottom: 20px;
}
.create-asisten-div {
  margin-bottom: 20px;
  width: 60%;
}
.create-asisten-button {
  padding: 10px 20px;
  font-size: 13pt;
  font-weight: bolder;
  background: none;
  border-style: none;
  background-color: #FFDD00;
  border-radius: 1000px;
  text-decoration: none;
}
/* TABLE SECTION */
.table-div {
  width: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
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
td#username {
  word-break: break-all;
}
.remove-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: red;
  background-color: red;
  border-radius: 1000px;
}
.remove-button:hover {
  background-color: white;
  color: red;
}
/* Pagination */
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
  width: 80px;
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
  min-width: 200px;
  max-width: 200px;
  text-align: center;
}
</style>
