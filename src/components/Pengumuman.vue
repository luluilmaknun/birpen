<template>
  <div>
    <modal
    name="detail-modal"
    :pivotX="0.0"
    >
      <div class="modal-container">
        It's me again, Nafis.
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

      <tr v-for="content in tableData" :key="content.id">
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
          <button v-on:click="showModal()" class="detail-button">
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
      tableHead: [
        'Mata Kuliah', 'Dosen', 'Sesi', 'Status', 'Aksi',
      ],
      tableData: [
        {id: 1, nama_mata_kuliah: 'PPL-A', nama_dosen: 'Ahmad Fauzan A.I',
          sesi: '08.00 - 10.30', nama_status_pengumuman: 'Terlambat'},
        {id: 2, nama_mata_kuliah: 'Alin', nama_dosen: 'Lulu',
          sesi: '10.00 - 12.30', nama_status_pengumuman: 'Dibatalkan'},
        {id: 3, nama_mata_kuliah: 'POK', nama_dosen: 'Ardho',
          sesi: '08.00 - 10.30', nama_status_pengumuman: 'Dibatalkan'},
      ],
      myArray: {
        namaMatkul: 'PPL', namaDosen: 'Napis', sesi: '08.00 - 10.30',
        statusPengumuman: 'Terlambat',
      },
    };
  },
  methods: {
    showModal() {
      this.$modal.show('detail-modal');
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
.modal-container {
  display: flex;
  flex-direction: column;
  align-items: center;
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
</style>
