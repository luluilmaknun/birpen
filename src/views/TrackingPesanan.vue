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
          <td id="id_pesanan">
            {{ data.id_pesanan }}
          </td>
          <td id="nama_mahasiswa">
            {{ data.nama_mahasiswa }}
          </td>
          <td id="npm_mahasiswa">
            {{ data.npm_mahasiswa }}
          </td>
          <td id="waktu_pemesanan">
            {{ data.waktu_pemesanan }}
          </td>
          <td id="status_bayar">
            {{ data.status_bayar }}
          </td>
          <td id="status_surat">
            {{ data.status_surat }}
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
        'Waktu Pemesanan', 'Status Bayar', 'Status Surat', 'Aksi',
      ],
      DUMMY_DATA: [
        {
          id_pesanan: 101,
          nama_mahasiswa: 'Athallah Annafis',
          npm_mahasiswa: '1706075022',
          waktu_pemesanan: '2 Januari 2020',
          status_bayar: 'Lunas',
          status_surat: 'Menunggu paraf manager pendidikan',
        },
        {
          id_pesanan: 102,
          nama_mahasiswa: 'Julia Ningrum',
          npm_mahasiswa: '1706075042',
          waktu_pemesanan: '3 Februari 2020',
          status_bayar: 'Lunas',
          status_surat: 'Selesai',
        },
        {
          id_pesanan: 103,
          nama_mahasiswa: 'Yusuf Tri Ardho',
          npm_mahasiswa: '1704052130',
          waktu_pemesanan: '4 Maret 2020',
          status_bayar: 'Belum Lunas',
          status_surat: 'Menunggu paraf manager pendidikan',
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
