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
        <tr v-for="data in DUMMY_DATA" :key="data.id">
          <td id="pk">
            {{ data.pk }}
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
            {{ data.status_bayar }}
          </td>
          <td id="aksi">
            <button class="detail-button">
              Detail
            </button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      tableHead: [
        'ID Pesanan', 'Nama Mahasiswa', 'NPM Mahasiswa',
        'Waktu Pemesanan', 'Status Bayar', 'Aksi',
      ],
      DUMMY_DATA: [
        {
          pk: 101,
          nama_pemesan: 'Athallah Annafis',
          npm_pemesan: '1706075022',
          waktu_pemesanan: '2 Januari 2020',
          status_bayar: 'Lunas',
        },
        {
          pk: 102,
          nama_pemesan: 'Julia Ningrum',
          npm_pemesan: '1706075042',
          waktu_pemesanan: '3 Februari 2020',
          status_bayar: 'Lunas',
        },
        {
          pk: 103,
          nama_pemesan: 'Yusuf Tri Ardho',
          npm_pemesan: '1704052130',
          waktu_pemesanan: '4 Maret 2020',
          status_bayar: 'Belum Lunas',
        },
      ],
    };
  },
  created: function() {

  },
  methods: {

  },
};
</script>

<style>
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
</style>
