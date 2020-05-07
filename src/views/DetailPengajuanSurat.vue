<template>
  <div>
    <div class="main-container">
      <div class="profile-detail">
        <div class="left-detail">
          <p>Nama</p>
          <p>NPM</p>
          <p>ID Pesanan</p>
        </div>
        <div class="right-detail">
          <p id="profile-nama">: {{ detailPesanan.nama_pemesan }}</p>
          <p id="profile-npm">: {{ detailPesanan.npm_pemesan }}</p>
          <p id="profile-idPesanan">
            : {{ String(detailPesanan.pk).padStart(6, '0') }}
          </p>
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
              Jumlah
            </th>
            <th>
              Status
            </th>
          </tr>

          <tr v-for="content in listPesanan"
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
      profileDetail: {
        nama: 'Athallah Annafis',
        npm: '1706075022',
        id_pesanan: 'OD1FC',
      },
      response: {},
      detailPesanan: {},
      listPesanan: [],
      idPesanan: 'undefined',
      isAdmin: localStorage.getItem('is_admin') === 'true',
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
  created: function() {
    this.idPesanan = this.getIdFromURL(window.location.href);
    this.fetchDetail(this.idPesanan);
  },
  methods: {
    getIdFromURL: function(theURL) {
      // https://pplukan.com/surat/tracking/idPesanan/detailPengajuanSurat
      const tempArr = theURL.split('/');
      const theID = tempArr[5];
      return theID;
    },
    fetchDetail: function(idPesanan) {
      trackingPesananApi.getDetailPesanan(idPesanan).then((result) => {
        this.detailPesanan = result.data;
        this.responseToList(
            this.detailPesanan.pesanan_surat_akademik, this.listPesanan
        );
      });
    },
    responseToList: function(theResponse, theList) {
      for (let i = 0; i < theResponse.length; i++) {
        this.$set(theList, i, theResponse[i]);
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
