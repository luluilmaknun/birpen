<template>
  <div v-if="isFetchAlumni">
    <img src="@/assets/icons/loader.svg"/>
  </div>
  <div v-else>
    <h1 class="title-alumni">
      Daftar Alumni
    </h1>

    <!-- TABLE SECTION -->
    <div class="table-div">
      <table aria-hidden="true">
        <tr>
          <th id="table-header" class="head-table"
            v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="alumni in renderPagedList" :key="alumni.username">
          <td id="username">
            {{ alumni.username }}
          </td>
          <td id="email">
              {{ alumni.email }}
          </td>
          <td id="status">
              <div v-if="alumni.blocked">Diblokir</div>
              <div v-else>Aktif</div>
          </td>
          <td>
            <ToggleBlockAlumni
            :alumni_username="alumni.username"
            :blocked="alumni.blocked"/>
          </td>
        </tr>
      </table>
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
import alumniServices from '@/services/alumniServices';
import ToggleBlockAlumni from '@/components/toggle-block-alumni';

export default {
  name: 'AlumniPage',
  components: {
    ToggleBlockAlumni,
  },
  data() {
    return {
      tableHead: [
        'Username', 'Email', 'Status', 'Aksi',
      ],
      listAlumni: [],
      response: {},
      isFetchAlumni: false,
      showPrev: true,
      showNext: true,
      showFirst: true,
      showLast: true,
      pagedList: [],
      renderPagedList: [],
      pageNumber: 1,
    };
  },
  created() {
    this.fetchAlumni();
  },
  methods: {
    fetchAlumni() {
      this.isFetchAlumni = true;
      alumniServices.fetchAlumni().then((result) => {
        this.response = result.data;
        for (let i = 0; i < this.response.alumni.length; i++) {
          this.$set(this.listAlumni, i, this.response.alumni[i]);
        }
        this.fetchPagination(this.listAlumni, this.pagedList);
        this.renderPagination(this.pageNumber, this.pagedList);
        this.isFetchAlumni = false;
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
.title-alumni {
  margin-top: 50px;
  margin-bottom: 20px;
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
  padding-left: 1em;
  padding-right: 1em;
  padding-top: 0.75em;
  padding-bottom: 0.75em;
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
@media only screen and (max-width: 539px) {
  .table-div {
    width: 75%;
  }
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
</style>
