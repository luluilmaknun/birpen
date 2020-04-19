<template>
  <div>
    <modal
    name="detail-modal"
    :pivotX="0.0"
    :pivotY="0.3"
    :height="750"
    :width="1000"
    >
    <div v-for="detail in modaldetail" :key="detail.pk" class="modal-container">
      <h1 style="margin-bottom:20px">Detail</h1>
        <div v-if="modaldetail[0].nama_asisten == ''" class="detail-container">
          <div id="left">
            <p>ID:</p>
            <p>Dibuat oleh:</p>
            <p>Waktu dibuat:</p>
            <p>Mata kuliah:</p>
            <p>Jenis:</p>
            <p>Dosen:</p>
            <p>Ruang:</p>
            <p>Sesi:</p>
            <p>Status:</p>
            <p>Komentar:</p>
          </div>

          <div id="right">
            <p id="pk">{{ detail.pk }}</p>
            <p>{{ detail.pembuat }}</p>
            <p>{{ detail.created_at }}</p>
            <p>{{ detail.nama_mata_kuliah }}</p>
            <p>{{ detail.jenis_pengumuman }}</p>
            <p>{{ detail.nama_dosen }}</p>
            <p>{{ detail.nama_ruang }}</p>
            <p>{{ detail.sesi }}</p>
            <p>{{ detail.nama_status_pengumuman }}</p>
            <p>{{ detail.komentar }}</p>
          </div>
        </div>

        <div v-else class="detail-container">
          <div id="left">
            <p>ID:</p>
            <p>Dibuat oleh:</p>
            <p>Waktu dibuat:</p>
            <p>Mata kuliah:</p>
            <p>Jenis:</p>
            <p>Dosen:</p>
            <p>Asisten:</p>
            <p>Ruang:</p>
            <p>Sesi:</p>
            <p>Status:</p>
            <p>Komentar:</p>
          </div>

          <div id="right">
            <p id="pk">{{ detail.pk }}</p>
            <p>{{ detail.pembuat }}</p>
            <p>{{ detail.created_at }}</p>
            <p>{{ detail.nama_mata_kuliah }}</p>
            <p>{{ detail.jenis_pengumuman }}</p>
            <p>{{ detail.nama_dosen }}</p>
            <p>{{ detail.nama_asisten }}</p>
            <p>{{ detail.nama_ruang }}</p>
            <p>{{ detail.sesi }}</p>
            <p>{{ detail.nama_status_pengumuman }}</p>
            <p>{{ detail.komentar }}</p>
          </div>
        </div>

        <div class="modal-button-container">
          <a :href="'/pengumuman/' + detail.pk + '/edit/'" class="edit-button"
          v-if='isAdmin ||
          ((isAsdos || isDosen) && (username === detail.pembuat))'>
            Ubah
          </a>
          <DeleteButton class="delete-button"
          v-if='isAdmin ||
          ((isAsdos || isDosen) && (username === detail.pembuat))'/>
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
      <a :href="'/pengumuman/create'"
      class="create-announcement-button"
      v-if='isAdmin || isAsdos || isDosen'>
        BUAT PENGUMUMAN
      </a><a v-else/>
      <div class="create-filter-spreader"></div>
      <FilterComponent/>
    </div>

    <!-- UNFILTERED TABLE -->
    <div class="table-div" id="unfiltered-table"
    v-if="!isFiltered">
      <!-- TODAY if no data -->
      <div class="table-div" id="table-today" v-if="today.length == 0">
        <p class="today-tomorrow-date">{{ todayDate }}</p>
        <!-- TODAY ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <!-- TODAY NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <h2>Tidak ada pengumuman</h2>
      </div>

      <!-- table if there are datas -->
      <div class="table-div" v-else>
        <p class="today-tomorrow-date">{{ todayDate }}</p>
        <!-- TODAY ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in today" :key="content.pk">
            <td id="nama_mata_kuliah_today">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_today">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_today">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_today">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
                Detail
              </button>
            </td>
            <td id="deleted_info">
              <p v-if="content.deleted != null" class="deleted-info">
                {{ modifyDateTime(String(content.deleted)) }}
              </p>
              <p v-else class="not-deleted-info">Not Deleted</p>
            </td>
          </tr>
        </table>
        <!-- TODAY NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in today" :key="content.pk">
            <td id="nama_mata_kuliah_today">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_today">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_today">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_today">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
                Detail
              </button>
            </td>
          </tr>
        </table>
      </div>

      <!-- TOMORROW -->
      <!-- table if no data -->
      <div class="table-div" id="table-tomorrow" v-if="tomorrow.length == 0">
        <p class="today-tomorrow-date">{{ tomorrowDate }}</p>
        <!-- TOMORROW ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <!-- TOMORROW NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <h2>Tidak ada pengumuman</h2>
      </div>

      <!-- table if there are datas -->
      <div class="table-div" id="table-tomorrow" v-else>
        <p class="today-tomorrow-date">{{ tomorrowDate }}</p>
        <!-- TOMORROW ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in tomorrow" :key="content.pk">
            <td id="nama_mata_kuliah_tomorrow">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_tomorrow">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_tomorrow">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_tomorrow">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
                Detail
              </button>
            </td>
            <td id="deleted_info">
              <p v-if="content.deleted != null" class="deleted-info">
                {{ modifyDateTime(String(content.deleted)) }}
              </p>
              <p v-else class="not-deleted-info">Not Deleted</p>
            </td>
          </tr>
        </table>
        <!-- TOMORROW NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in tomorrow" :key="content.pk">
            <td id="nama_mata_kuliah_tomorrow">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_tomorrow">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_tomorrow">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_tomorrow">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
                Detail
              </button>
            </td>
          </tr>
        </table>
      </div>
    </div>

    <!-- FILTERED TABLE  -->
    <div class="table-div" id="filtered-table" v-else>
      <!-- if there is no data -->
      <div class="table-div" v-if="filteredAnnouncement.length == 0">
        <p class="today-tomorrow-date">{{ filterDate }}</p>
        <!-- FILTERED ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <!-- FILTERED NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>
          <tr>
            <td/>
          </tr>
        </table>
        <h2>Tidak ada pengumuman</h2>
      </div>


      <!-- if there are datas -->
      <div class="table-div" v-else>
        <p class="today-tomorrow-date">{{ filterDate }}</p>
        <!-- FILTERED ADMIN -->
        <table v-if="isAdmin" aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in adminHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in filteredAnnouncement" :key="content.pk">
            <td id="nama_mata_kuliah_filtered">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_filtered">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_filtered">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_filtered">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
                Detail
              </button>
            </td>
            <td id="deleted_info">
              <p v-if="content.deleted != null" class="deleted-info">
                {{ modifyDateTime(String(content.deleted)) }}
              </p>
              <p v-else class="not-deleted-info">Not Deleted</p>
            </td>
          </tr>
        </table>
        <!-- FILTERED NON ADMIN -->
        <table v-else aria-hidden="true">
          <tr>
            <th id="table-header" class="head-table"
              v-for="head in tableHead" :key="head">
              {{ head }}
            </th>
          </tr>

          <tr v-for="content in filteredAnnouncement" :key="content.pk">
            <td id="nama_mata_kuliah_filtered">
              {{ content.nama_mata_kuliah }}
            </td>
            <td id="nama_dosen_filtered">
              {{ content.nama_dosen }}
            </td>
            <td id="nama_sesi_filtered">
              {{ content.nama_sesi }}
            </td>
            <td id="nama_status_pengumuman_filtered">
              {{ content.nama_status_pengumuman }}
            </td>
            <td id="action">
              <button
              v-on:click="showModal(
                content.pk,
                content.pembuat,
                content.created_at,
                content.nama_mata_kuliah,
                content.jenis_pengumuman,
                content.nama_dosen,
                content.nama_asisten,
                content.nama_ruang,
                content.nama_sesi,
                content.nama_status_pengumuman,
                content.komentar,
                content.deleted)" class="detail-button" id="detail-btn">
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
import DeleteButton from '@/components/delete';
import FilterComponent from '@/components/date-picker';
import announcementApi from '@/services/announcementServices';

export default {
  data: function() {
    return {
      username: localStorage.getItem('username'),
      isDosen: localStorage.getItem('role') === 'staff',
      isAsdos: localStorage.getItem('is_asdos') === 'true',
      isAdmin: localStorage.getItem('is_admin') === 'true',
      modaldetail: [
        {
          pk: 999,
          deleted: null,
          pembuat: '',
          created_at: '',
          nama_mata_kuliah: '',
          jenis_pengumuman: '',
          nama_dosen: '',
          nama_asisten: '',
          nama_ruang: '',
          sesi: '',
          nama_status_pengumuman: '',
          komentar: '',
        },
      ],
      tableHead: [
        'Mata Kuliah', 'Dosen', 'Sesi', 'Status', 'Aksi',
      ],
      adminHead: [
        'Mata Kuliah', 'Dosen', 'Sesi', 'Status', 'Aksi', 'Deleted Time',
      ],
      response: {},
      filteredResponse: {},
      today: [],
      tomorrow: [],
      filteredAnnouncement: [],
      isFiltered: false,
      todayDate: '',
      tomorrowDate: '',
      filterDate: '',
      error_msg: '',
    };
  },
  created: function() {
    this.fetchData();
    this.getTodayTomorrowDate();
  },
  methods: {
    fetchData: function() {
      const currentURL = window.location.href;
      const arr = currentURL.split('tanggal=');
      const date = arr[1];
      if (typeof(date) == 'undefined') {
        this.isFiltered = false;
        this.fetchPengumuman();
      } else {
        this.isFiltered = true;
        this.fetchFilteredPengumuman(date);
      }
    },
    fetchFilteredPengumuman: function(date) {
      const dateResult = this.getDateWithMonthName(date);
      this.filterDate = dateResult;
      announcementApi.getAnnouncementFiltered(date).then((result) => {
        this.response = result.data;
        for (let i = 0; i < this.response.pengumuman_response.length; i++) {
          this.$set(
              this.filteredAnnouncement, i, this.response.pengumuman_response[i]
          );
        }
      });
    },
    fetchPengumuman: function() {
      announcementApi.getAnnouncementDefault().then((d) => {
        this.response = d.data;
        this.responseToList(this.response.pengumuman_today, this.today);
        this.responseToList(this.response.pengumuman_tomo, this.tomorrow);
      }).catch((error) => {
        this.error_msg = error.response.data.detail;
      });
    },
    responseToList: function(theResponse, theList) {
      for (let i = 0; i < theResponse.length; i++) {
        this.$set(theList, i, theResponse[i]);
      }
    },
    getMonthName: function(monthNumber) {
      const mlist = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];
      return mlist[monthNumber];
    },
    getDateWithMonthName: function(theDate) {
      const temp = theDate.split('-');
      const day = temp[0]; const month = this.getMonthName(parseInt(temp[1]));
      const year = temp[2];
      const result = day + ' ' + month + ' ' + year;
      return result;
    },
    showModal(pk, pembuat, created, matkul, jenis, dosen, asisten,
        ruang, sesi, status, komentar, deleted) {
      const data = this.modaldetail[0];
      this.$modal.show('detail-modal');
      data.pk = pk;
      data.deleted = deleted
      data.pembuat = pembuat;
      data.created_at = this.modifyDateTime(created);
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
    getTodayTomorrowDate: function() {
      const currentDay = new Date();

      let date = currentDay.getDate();
      let month = currentDay.getMonth();
      let year = currentDay.getFullYear();
      this.todayDate = date + ' ' + this.getMonthName(month) + ' ' + year;

      // next day
      const nextDay = new Date(currentDay);
      nextDay.setDate(currentDay.getDate() + 1);
      date = nextDay.getDate();
      month = nextDay.getMonth();
      year = nextDay.getFullYear();
      this.tomorrowDate = date + ' ' + this.getMonthName(month) + ' ' + year;
    },
    modifyDateTime: function(time) {
      const datetime = String(time);
      const timestampList = datetime.split('T');
      const timeList = timestampList[1].split(':');

      // Date and time
      const second = timeList[2].split('.')[0];
      const createdTime = timeList[0] + ':' + timeList[1] + ':' + second;
      const date = timestampList[0];
      const result = date + '  ' + createdTime;
      return result;
    },
  },
  components: {
    DeleteButton,
    FilterComponent,
  },
};
</script>

<style scoped>
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
.today-tomorrow-date {
  margin-bottom: 15px;
  font-size: 15pt;
  font-weight: bolder;
}
.table-div {
  width: 85%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.table-div h2 {
  color: black;
  font-size: 15pt;
}
#table-tomorrow {
  margin-top: 80px;
  margin-bottom: 100px;
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
  justify-content: center;
}
.detail-container #left {
  margin-right: 20px;
  font-weight: bolder;
}
.detail-container #right {
  margin-right: 500px;
}
.modal-button-container {
  display: flex;
  flex-direction: row;
  margin-top: 140px;
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
  padding: 5px 15px;
  font-size: 20pt;
  border-radius: 1000px;
  border-color: #7584D1;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
  text-decoration: none;
  font-weight: bolder;
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
.deleted-info {
  color: red;
  font-weight: bolder;
}
.not-deleted-info {
  color: green;
  font-weight: bolder;
}
</style>
