<template>
  <div>
    <div class="table-div">
      <h2>Daftar Pengajuan Surat</h2>
      <table>
        <tr>
          <th v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>
        <tr v-for="data in this.trackingList" :key="data.id">
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

      <div class="pagination-section">
        <button>Prev</button>
        {{ pageNumber }}
        <button>Next</button>
      </div>
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
      tableHead: [
        'ID Pesanan', 'Nama Mahasiswa', 'NPM Mahasiswa',
        'Waktu Pemesanan', 'Status Bayar', 'Aksi',
      ],
      response: {},
      trackingList: [],
      pagedTrackingList: [],
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
        this.fetchPagination(this.trackingList, this.pagedTrackingList);
        // Perform modify created date
        this.fetchDateCreated(this.trackingList, 'waktu_pemesanan');
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
        modDate = this.getDate(theList[i].waktu_pemesanan);
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
      const temp = this.modifyDateTime(dateAndTime);
      const tempArr = temp.split(' ');
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
      const result = date + '  ' + createdTime;
      return result;
    },
    fetchPagination: function(theList, paginationList) {
      const base = 5;
      let temp = [];
      let count = 0;
      for (let i = 0; i < theList.length; i++) {
        temp.push(theList[i]);
        count += 1;
        if (count == base) {
          count = 0;
          paginationList.push(temp);
          temp = [];
        } if (i == theList.length-1) {
          paginationList.push(temp);
          temp = [];
        }
      }
      console.log(paginationList);
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
  margin-bottom: 100px;
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
</style>
