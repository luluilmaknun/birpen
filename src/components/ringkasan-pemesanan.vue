<template>
  <div id="ringkasan-pemesanan">
    <h2 class="title">Ringkasan</h2>
    <br>
    <br>
    <!-- TABLE SECTION -->
    <div class="table-div">
      <table aria-hidden="true">
        <tr>
          <th class="head-table"
            v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="pesanan in daftar_pesanan" :key="pesanan.id">
          <td class="jenis_dokumen">
            {{ pesanan.jenis_dokumen }}
          </td>
          <td class="harga">
            Rp. {{ pesanan.harga }}
          </td>
          <td class="jumlah">
            {{ pesanan.jumlah }}
          </td>
        </tr>

        <tr id="jumlah">
          <td></td>
          <td class="harga">
            <span>Jumlah: </span>Rp. {{ this.jumlah }}
          </td>
          <td></td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RingkasanPemesanan',
  props: {
    daftar_pesanan: Object,
    jumlah: String,
  },
  data: function() {
    return {
      tableHead: ['Jenis Dokumen', 'Harga', 'Jumlah'],
    };
  },
};
</script>

<style>
#ringkasan-pemesanan .title {
  font-weight: bold;
  font-size: 40px;
  line-height: 73px;
  text-align: center;
  color: black;
}
/* TABLE SECTION */
.table-div {
  width: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
}
.table-div table {
  border-radius: 1em;
  text-align: center;
  overflow: hidden;
  border-collapse: collapse;
  width: 100%;
}
th, td {
  padding-left: 1em;
  padding-right: 1em;
  padding-top: 0.75em;
  padding-bottom: 0.75em;
}
th {
  background-color: #2D3033;
  font-weight: bolder;
  color: white;
}
th, tr {
  font-size: 10pt;
}
tr:nth-child(odd) {
  background-color: #D3D3D3;
}
td.jenis_dokumen {
  word-break: break-all;
}
th:first-of-type, td.jenis_dokumen, td.harga {
  text-align: left;
}
th:first-of-type, td.jenis_dokumen {
  padding-left: 30px;
  width: 60%;
}
th:nth-of-type(2), td.harga {
  width: 20%;
}
th:nth-of-type(3), td.jumlah {
  width: 10%;
  padding-right: 8%;
  text-align: center;
}
tr#jumlah {
  background-color: white;
}
tr#jumlah td.harga {
  font-weight: bolder;
}
tr#jumlah td.harga span {
  margin-left: -69px;
  margin-right: 10px;
}
@media only screen and (max-width: 539px) {
  .table-div {
    width: 75%;
  }
}
</style>
