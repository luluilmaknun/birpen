<template>
  <div>
    <div class="main-container">
      <div class="profile-detail">
        <div class="left-detail">
          <p>Nama:</p>
          <p>NPM:</p>
          <p>ID Pesanan:</p>
        </div>
        <div class="right-detail">
          <p id="profile-nama">{{ profileDetail.nama }}</p>
          <p id="profile-npm">{{ profileDetail.npm }}</p>
          <p id="profile-idPesanan">{{ profileDetail.id_pesanan }}</p>
        </div>
      </div>
      <!-- table -->
      <div class="table-tracking-div">
        <table>
          <tr>
            <th id="table-header" class="head-table">
              Nama Surat
            </th>
            <th>
              Status
            </th>
          </tr>

          <tr v-for="content in listSuratTransfered"
          :key="content.status_surat">
            <td id="nama_surat">
              {{ content.surat_akademik }}
            </td>
            <td id="nama_status_surat">
              {{ content.status_surat }}
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import trackingPesananApi from '@/services/trackingPesananServices.js';

export default {
  created: function() {

  },
  data: function() {
    return {
      profileDetail: {
        nama: 'Athallah Annafis',
        npm: '1706075022',
        id_pesanan: 'OD1FC',
      },
      response: {},
      listPesanan: [],
      DUMMY_DATA: [
        {
          nama_surat: 'Transkrip nilai',
          nama_status_surat: 'Menunggu paraf dari Wakil Dekan',
        },
        {
          nama_surat: 'Keterangan Mahasiswa FIB UI',
          nama_status_surat: 'Selesai',
        },
      ],
    };
  },
  methods: {
    fetchPesanan() {
      trackingPesananApi.getTrackingPesanan().then((result) => {
        this.response = result;
      });
    },
  },
};
</script>

<style>
.main-container {
  width: 60%;
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
</style>
