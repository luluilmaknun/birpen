<template>
  <div>
    <div class="table-div">
      <h2>Daftar Pengajuan Surat</h2>
      <table>
        <tr>
          <th id="table-head" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>
        <tr v-for="data in renderPagedTrackingList" :key="data.pk">
          <td id="pk">
            {{ String(data.pk).padStart(6, '0') }}
          </td>
          <td id="nama_pemesan">
            {{ data.nama_pemesan }}
          </td>
          <td id="npm_pemesan">
            {{ data.npm_pemesan }}
          </td>
          <td id="waktu_pemesanan">
            {{ data.waktu_pemesanan }}
          </td>
          <td id="status_bayar">
            <div v-if="isAdmin" class="status-bayar-div">
              {{ data.status_bayar }}
              <EditStatusBayar
              :id_pesanan="String(data.pk).padStart(6, '0')"
              :status_bayar="data.status_bayar"/>
            </div>
            <div class="status-bayar-div" v-else>
              {{ data.status_bayar }}
            </div>
          </td>
          <td id="aksi">
            <button
            v-on:click="showDetailPage(data.pk)"
            class="detail-button">
              Detail
            </button>
          </td>
        </tr>
      </table>
    </div>
    <div class="pagination-section">
      <button class="pagination-button"
      id="prev-button" v-show="showPrev" v-on:click="this.decreamentPage">
        &lt;
      </button>
      <p class="page-number">{{ pageNumber }}</p>
      <button class="pagination-button"
      id="next-button" v-show="showNext" v-on:click="this.increamentPage">
        &gt;
      </button>
    </div>
  </div>
</template>

<script>
import EditStatusBayar from '@/components/edit-status-bayar.vue';
import trackingPesananApi from '@/services/suratServices.js';
export default {
  components: {
    EditStatusBayar,
  },
  data: function() {
    return {
      showPrev: true,
      showNext: true,
      tableHead: [
        'ID Pesanan', 'Nama Mahasiswa', 'NPM Mahasiswa',
        'Waktu Pemesanan', 'Status Bayar', 'Aksi',
      ],
      response: {},
      trackingList: [],
      pagedTrackingList: [],
      renderPagedTrackingList: [],
      pageNumber: 1,
      errorResponse: {},
      isAdmin: localStorage.getItem('is_admin') === 'true',
    };
  },
  created: function() {
    this.fetchTrackingPesanan();
  },
  methods: {
    fetchTrackingPesanan: function() {
      trackingPesananApi.getTrackingPesanan().then((result) => {
        this.response = result.data;
        this.responseToList(this.response.pesanan, this.trackingList);
        // Perform modify created date
        this.fetchDateCreated(this.trackingList, 'waktu_pemesanan');
        this.fetchPagination(this.trackingList, this.pagedTrackingList);
        this.renderPagination(this.pageNumber, this.pagedTrackingList);
      }).catch((error) => {
        this.errorResponse = error.data;
      });
    },
    responseToList: function(theResponse, theList) {
      for (let i = 0; i < theResponse.length; i++) {
        this.$set(theList, i, theResponse[i]);
      }
    },
    showDetailPage: function(pk) {
      this.$router.push('/surat/tracking/' + pk + '/detail/');
    },
    fetchDateCreated: function(theList, columnTarget) {
      let modDate;
      for (let i = 0; i < theList.length; i++) {
        modDate = this.modifyDateTime(theList[i].waktu_pemesanan);
        this.$set(theList[i], columnTarget, modDate);
      }
    },
    getMonthName: function(monthNumber) {
      const choice = monthNumber - 1;
      const month = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
        'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
      return month[choice];
    },
    getDate: function(dateAndTime) {
      const tempArr = dateAndTime.split(' ');
      const dateArr = tempArr[0].split('-');
      // Perform date formating
      const day = dateArr[2];
      const monthNumber = dateArr[1];
      const month = this.getMonthName(monthNumber);
      const year = dateArr[0];
      const result = day + ' ' + month + ' ' + year;
      return result;
    },
    modifyDateTime: function(defaultTime) {
      const datetime = String(defaultTime);
      const timestampList = datetime.split('T');
      const timeList = timestampList[1].split(':');

      // Date and time
      const second = timeList[2].split('.')[0];
      const createdTime = timeList[0] + ':' + timeList[1] + ':' + second;
      const date = timestampList[0];
      const result = date + ' ' + createdTime;
      const temp = this.getDate(result);
      return temp;
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
      this.renderPagedTrackingList = tempList;
    },
    increamentPage: function() {
      this.pageNumber++;
      this.renderPagination(this.pageNumber, this.pagedTrackingList);
    },
    decreamentPage: function() {
      this.pageNumber--;
      this.renderPagination(this.pageNumber, this.pagedTrackingList);
    },
    checkPaginationButton: function(pageNumber, pagedList) {
      if (pageNumber == 1 &&
      (pagedList.length == 1 || pagedList.length == 0)) {
        this.showPrev = false;
        this.showNext = false;
      } else if (pageNumber == 1 && pagedList.length > 1) {
        // ujung kiri
        this.showPrev = false;
        this.showNext = true;
      } else if (pageNumber == pagedList.length) {
        // ujung kanan
        this.showNext = false;
        this.showPrev = true;
      } else {
        // tengah
        this.showNext = true;
        this.showPrev = true;
      }
    },
  },
};
</script>

<style scoped>
.table-div h2 {
  color: black;
  margin-bottom: 20px;
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
.table-div {
  width: 85%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  min-height: 650px;
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
.status-bayar-div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.pagination-section {
  margin-top: 30px;
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
  align-content: center;
  color: black;
  font-weight: bolder;
  font-size: 16pt;
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
.page-number {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
