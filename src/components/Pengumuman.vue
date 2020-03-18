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
            <p>{{ temp[0].pembuat }}</p>
            <p>{{ temp[0].timestamp }}</p>
            <p>{{ temp[0].nama_mata_kuliah }}</p>
            <p>{{ temp[0].jenis_pengumuman }}</p>
            <p>{{ temp[0].nama_dosen }}</p>
            <p>{{ temp[0].nama_ruang }}</p>
            <p>{{ temp[0].sesi }}</p>
            <p>{{ temp[0].nama_status_pengumuman }}</p>
            <p>{{ temp[0].komentar }}</p>
          </div>
        </div>

        <div class="modal-button-container">

        </div>
    </div>
    </modal>

    <h1 class="title-pengumuman">
      Pengumuman
    </h1>

    <table>
      <tr>
        <th class="head-table" v-for="head in tableHead" :key="head">
          {{ head }}
        </th>
      </tr>

      <tr v-for="content in tableData" :key="content.pk">
        <td>
          {{ content.nama_mata_kuliah }}
        </td>
        <td>
          {{ content.nama_dosen }}
        </td>
        <td>
          {{ content.sesi }}
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
            content.nama_ruang,
            content.sesi,
            content.nama_status_pengumuman,
            content.komentar)" class="detail-button">
            Detail
          </button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      temp: [
        {
          pk: 999,
          pembuat: '',
          timestamp: '',
          nama_mata_kuliah: '',
          jenis_pengumuman: '',
          nama_dosen: '',
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
        {
          pk: 1,
          pembuat: 'Ardho',
          timestamp: '18/07/2020 08:33:02',
          nama_mata_kuliah: 'PPL-A',
          jenis_pengumuman: 'Asistensi',
          nama_dosen: 'Ahmad Fauzan A.I',
          nama_ruang: '1203',
          sesi: '08.00 - 10.30',
          nama_status_pengumuman: 'Terlambat',
          komentar: 'Saya ketiduran',
        },
        {
          pk: 2,
          pembuat: 'Nafis',
          timestamp: '18/07/2020 08:33:01',
          nama_mata_kuliah: 'Alin',
          jenis_pengumuman: 'Perkuliahan',
          nama_dosen: 'Lulu',
          nama_ruang: '2203',
          sesi: '10.00 - 12.30',
          nama_status_pengumuman: 'Dibatalkan',
          komentar: 'Macet',
        },
        {
          pk: 3,
          pembuat: 'Juli',
          timestamp: '18/07/2020 08:33:00',
          nama_mata_kuliah: 'POK',
          jenis_pengumuman: 'Perkuliahan',
          nama_dosen: 'Ardho',
          nama_ruang: '1203',
          sesi: '08.00 - 10.30',
          nama_status_pengumuman: 'Terlambat',
          komentar: 'Saya ketiduran',
        },
      ],
    };
  },
  methods: {
    showModal(pk, pembuat, timestamp, matkul, jenis, dosen,
        ruang, sesi, status, komentar) {
      const data = this.temp[0];
      this.$modal.show('detail-modal');
      data.pk = pk;
      data.pembuat = pembuat;
      data.timestamp = timestamp;
      data.nama_mata_kuliah = matkul;
      data.nama_dosen = dosen;
      data.nama_ruang = ruang;
      data.sesi = sesi;
      data.jenis_pengumuman = jenis;
      data.nama_status_pengumuman = status;
      data.komentar = komentar;
    },
  },
};
</script>

<style>
.title-pengumuman {
  margin-top: 50px;
  margin-bottom: 20px;
}
table {
  border-radius: 1em;
  text-align: center;
  overflow: hidden;
  border-collapse: collapse;
  width: 85%;
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
  margin: 10px;
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
}
</style>
