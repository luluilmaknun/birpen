<template>
  <div v-if="isFetchDetail">
    <img src="@/assets/icons/loader.svg"/>
  </div>
  <div v-else>
    <div class="main-container">
      <div class="profile-detail">
        <div class="left-detail">
          <p>Nama: </p>
          <p>NPM: </p>
          <p>ID Pesanan: </p>
        </div>
        <div class="right-detail">
          <p id="profile-nama">
            <b>{{ detailPesanan.nama_pemesan }}</b>
          </p>

          <p id="profile-npm">
            <b>{{ detailPesanan.npm_pemesan }}</b>
          </p>

          <p id="profile-idPesanan">
            <b>{{ String(detailPesanan.pk).padStart(6, '0') }}</b>
          </p>
        </div>
      </div>
      <!-- table -->
      <div class="table-tracking-div">
        <table aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table">
              Nama Surat
            </th>
            <th id="jumlah-header">
              Jumlah
            </th>
            <th id="status-header">
              Status
            </th>
          </tr>

          <tr v-for="content in renderPagedList"
          :key="content.surat_akademik">
            <td id="nama_surat">
              {{ content.surat_akademik }}
            </td>
            <td id="jumlah_surat">
              {{ content.jumlah }}
            </td>
            <td id="nama_status_surat">
              <div
              v-if="isAdmin"
              class="edit-status-surat-div">
                {{ content.status_surat }}
                <EditStatusSurat
                :id_pesanan="idPesanan"
                :status_surat="content.status_surat"
                :jenis_dokumen="content.surat_akademik"
                />
              </div>
              <div v-else class="edit-status-surat-div">
                {{ content.status_surat }}
              </div>
            </td>
          </tr>
        </table>
      </div>
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
import EditStatusSurat from '@/components/edit-status-surat.vue';
import trackingPesananApi from '@/services/suratServices.js';

export default {
  components: {
    EditStatusSurat,
  },
  data: function() {
    return {
      response: {},
      detailPesanan: {},
      listPesanan: [],
      idPesanan: 'undefined',
      isAdmin: localStorage.getItem('is_admin') === 'true',
      isFetchDetail: false,
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
    this.idPesanan = this.getIdFromURL(window.location.href);
    this.fetchDetail(this.idPesanan);
  },
  methods: {
    getIdFromURL: function(theURL) {
      const tempArr = theURL.split('/');
      const theID = tempArr[5];
      return theID;
    },
    fetchDetail: function(idPesanan) {
      this.isFetchDetail = true;
      trackingPesananApi.getDetailPesanan(idPesanan).then((result) => {
        this.detailPesanan = result.data;
        this.responseToList(
            this.detailPesanan.pesanan_surat_akademik, this.listPesanan
        );
        this.fetchPagination(this.listPesanan, this.pagedList);
        this.renderPagination(this.pageNumber, this.pagedList);
        this.isFetchDetail = false;
      });
    },
    responseToList: function(theResponse, theList) {
      for (let i = 0; i < theResponse.length; i++) {
        this.$set(theList, i, theResponse[i]);
      }
    },
    fetchPagination: function(theList, pagedList) {
      const base = 3;
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
.main-container {
  width: 60%;
}
.edit-status-surat-div {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.profile-detail {
  display: flex;
  margin-top: 20px;
  flex-direction: row;
  justify-content: left;
  width: 100%;
  line-height: 26pt;
}
.left-detail, .right-detail {
  margin: 0;
  margin-left: 10px;
  margin-right: 10px;
}
/* table styling */
.table-tracking-div {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 30px;
}
.table-tracking-div table {
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
