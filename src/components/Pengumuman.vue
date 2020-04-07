<template>
  <div>
    <modal
    name="detail-modal"
    :pivotX="0.0"
    :pivotY="0.3"
    :height="700"
    :width="1000"
    >
    <div class="modal-container">
      <h1 style="margin-bottom:20px">Detail</h1>
        <div class="detail-container">
          <div id="left">
            <p>Dibuat oleh:</p>
            <p>Timestamp:</p>
            <p>Mata kuliah:</p>
            <p>Jenis:</p>
            <p>Dosen:</p>
            <p>Ruang:</p>
            <p>Sesi:</p>
            <p>Status:</p>
            <p>Komentar:</p>
          </div>

          <div id="right">
            <p>{{ modaldetail[0].pembuat }}</p>
            <p>{{ modaldetail[0].timestamp }}</p>
            <p>{{ modaldetail[0].nama_mata_kuliah }}</p>
            <p>{{ modaldetail[0].jenis_pengumuman }}</p>
            <p>{{ modaldetail[0].nama_dosen }}</p>
            <p>{{ modaldetail[0].nama_ruang }}</p>
            <p>{{ modaldetail[0].sesi }}</p>
            <p>{{ modaldetail[0].nama_status_pengumuman }}</p>
            <p>{{ modaldetail[0].komentar }}</p>
          </div>
        </div>

        <div class="modal-button-container">
          <button class="edit-button">
            Ubah
          </button>
          <DeleteButton class="delete-button"/>
          <div class="spreader-button" />
          <button class="close-modal" v-on:click="closeModal()">
            Tutup
          </button>
        </div>
    </div>
    </modal>

<!-- TABLE SECTION -->
    <h1 class="title-pengumuman">
      Pengumuman
    </h1>

    <div class="create-filter-section">
      <router-link :to="{ name: 'create-pengumuman' }"
      class="create-announcement-button">
        BUAT PENGUMUMAN
      </router-link>
      <div class="create-filter-spreader"></div>
      <FilterComponent/>
    </div>

    <!-- TODAY -->
    <!-- table if no data -->
    <div class="table-div" v-if="today.length == 0">
      <table>
        <tr>
          <th class="head-table" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>
      <h2>Tidak ada pengumuman</h2>
    </div>

    <!-- table if there are datas -->
    <div class="table-div" v-else>
      <table>
        <tr>
          <th class="head-table" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="content in today" :key="content.pk">
          <td>
            {{ content.nama_mata_kuliah }}
          </td>
          <td>
            {{ content.nama_dosen }}
          </td>
          <td>
            {{ content.nama_sesi }}
          </td>
          <td>
            {{ content.nama_status_pengumuman }}
          </td>
          <td>
            <button
            v-on:click="showModal(
              content.pk,
              content.pembuat,
              content.created_at,
              content.nama_mata_kuliah,
              content.jenis_pengumuman,
              content.nama_dosen,
              content.nama_ruang,
              content.nama_sesi,
              content.nama_status_pengumuman,
              content.komentar)" class="detail-button">
              Detail
            </button>
          </td>
        </tr>
      </table>
    </div>

    <!-- TOMORROW -->
    <!-- table if no data -->
    <div class="table-div" id="table-tomorrow" v-if="tomorrow.length == 0">
      <table>
        <tr>
          <th class="head-table" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>
      <h2>Tidak ada pengumuman</h2>
    </div>

    <!-- table if there are datas -->
    <div class="table-div" id="table-tomorrow" v-else>
      <table>
        <tr>
          <th class="head-table" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="content in tomorrow" :key="content.pk">
          <td>
            {{ content.nama_mata_kuliah }}
          </td>
          <td>
            {{ content.nama_dosen }}
          </td>
          <td>
            {{ content.nama_sesi }}
          </td>
          <td>
            {{ content.nama_status_pengumuman }}
          </td>
          <td>
            <button
            v-on:click="showModal(
              content.pk,
              content.pembuat,
              content.timestamp,
              content.nama_mata_kuliah,
              content.jenis_pengumuman,
              content.nama_dosen,
              content.nama_asisten,
              content.nama_ruang,
              content.nama_sesi,
              content.nama_status_pengumuman,
              content.komentar)" class="detail-button">
              Detail
            </button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import DeleteButton from '@/components/delete';
import FilterComponent from '@/components/date-picker';
import announcementDataDefaultApi from '@/services/pengumumanDataService';

export default {
  data: function() {
    return {
      // TEST DATA SECTION
      modaldetail: [
        {
          pk: 999,
          pembuat: '',
          timestamp: '',
          nama_mata_kuliah: '',
          jenis_pengumuman: '',
          nama_dosen: '',
          nama_asisten:'',
          nama_ruang: '',
          sesi: '',
          nama_status_pengumuman: '',
          komentar: '',
        },
      ],
      tableHead: [
        'Mata Kuliah', 'Dosen', 'Sesi', 'Status', 'Aksi',
      ],
      tableData: [

      ],
      response: {},
      today: [],
      tomorrow: [],
    };
  },
  created: function() {
    this.fetchData();
  },
  methods: {
    fetchData: function() {
      announcementDataDefaultApi.fetch().then((d) => {
        // TODO GET ANNOUNCEMENTS IN DEFAULT
        this.response = d.data;
        // console.log(this.response.pengumuman_today[1]);
        for (let i = 0; i < this.response.pengumuman_today.length; i++) {
          this.$set(this.today, i, this.response.pengumuman_today[i]);
        }

        for (let i = 0; i < this.response.pengumuman_tomo.length; i++) {
          this.$set(this.tomorrow, i, this.response.pengumuman_tomo[i]);
        }

        console.log(this.today);
      });
    },
    showModal(pk, pembuat, created_at, matkul, jenis, dosen, asisten,
        ruang, sesi, status, komentar) {
      const data = this.modaldetail[0];
      // console.log(data);
      this.$modal.show('detail-modal');
      data.pk = pk;
      data.pembuat = pembuat;
      data.timestamp = created_at;
      data.nama_mata_kuliah = matkul;
      data.nama_dosen = dosen;
      data.nama_asisten = asisten;
      data.nama_ruang = ruang;
      data.sesi = sesi;
      data.jenis_pengumuman = jenis;
      data.nama_status_pengumuman = status;
      data.komentar = komentar;
    },
    closeModal() {
      this.$modal.hide('detail-modal');
    },
    getTodayDate() {
      var date = new Date();
      return date;
    }
  },
  components: {
    DeleteButton,
    FilterComponent,
  },
};
</script>

<style>
.title-pengumuman {
  margin-top: 50px;
  margin-bottom: 20px;
}
.create-filter-section {
  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: center;
  margin-bottom: 30px;
  width: 75%;
}
.create-filter-section .create-announcement-button {
  background: none;
  border-style: solid;
  border-color: #FFDD00;
  background-color: #FFDD00;
  padding: 10px 10px;
  border-width: 1.5px;
  font-weight: bolder;
  color: black;
  text-decoration: none;
  font-size: 10pt;
  border-radius: 1000px;
}
.create-filter-section .create-announcement-button:hover {
  border-color: greenyellow;
  background-color: greenyellow;
}
.table-div {
  width: 85%;
}
#table-tomorrow {
  margin-top: 100px;
}
#table-tomorrow h2 {
  color: black;
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

/* MODAL SECTION */
.modal-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 30px;
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
.detail-container {
  display:flex;
  flex-direction: row;
  line-height: 30pt;
}
.detail-container #left {
  margin-right: 20px;
  font-weight: bolder;
}
.detail-container #right {
  margin-right: 500px;
}
.detail-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.modal-button-container {
  display: flex;
  flex-direction: row;
  margin-top: 150px;
  align-items: center;
  align-content: center;
}
.modal-button-container button {
  padding: 5px 15px;
  border-style: none;
  background: none;
  font-weight: bolder;
  border-radius: 1000px;
  font-size: 20pt;
}
.modal-button-container .close-modal {
  background-color: #2D3033;
  border-style: solid;
  border-color: #2D3033;
  color: white;
}
.modal-button-container .close-modal:hover {
  background-color: rgb(233, 233, 233);
  border-color: #2D3033;
  color: #2D3033;
}
.modal-button-container .edit-button {
  background-color: #7584D1;
  border-style: solid;
  border-color: #7584D1;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
}
.modal-button-container .edit-button:hover {
  color: #7584D1;
  background-color: white;
}
/* .modal-button-container button:hover {
  background-color: rgb(105, 105, 105);
} */
.spreader-button {
  margin-left: 200px;
  margin-right: 200px;
}
</style>
