<template>
  <div>

    <h1 class="title-asdos">
      Daftar Asisten
    </h1>

    <div class="create-asisten-div">
      <CreateAsisten/>
    </div>
    <!-- TABLE SECTION -->
    <div class="table-div">
      <table>
        <tr>
          <th class="head-table" v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="asisten in listAsdos" :key="asisten.pk">
          <td id="nama_asisten">
            {{ asisten.nama_asisten }}
          </td>
          <td id="user_name">
            {{ asisten.user_name }}
          </td>
          <td id="nama_role">
            {{ asisten.nama_role }}
          </td>
          <td>
            <button
            class="remove-button" id="remove-btn">
              Hapus
            </button>
          </td>
        </tr>
      </table>
    </div>

  </div>
</template>

<script>
import assistenServices from '@/services/asistenServices';
import CreateAsisten from '@/components/tambah-asisten';

export default {
  name: 'AsdosPage',
  data: function() {
    return {
      tableHead: [
        'Nama Asisten', 'User name', 'Role', 'Aksi',
      ],
      listAsdos: [
        {
          'pk': 0,
          'nama_asisten': 'Alya Zahra',
          'user_name': 'alya.zahra',
          'nama_role': 'Asisten',
        },
        {
          'pk': 1,
          'nama_asisten': 'Athallah Annafis',
          'user_name': 'athallah.annafis',
          'nama_role': 'Asisten',
        },
        {
          'pk': 2,
          'nama_asisten': 'Ahmad Fauzan',
          'user_name': 'ahmad.fauzan',
          'nama_role': 'Asisten',
        },
      ],
      response: {},
    };
  },
  created: function() {
    this.fetchAsdos();
  },
  methods: {
    fetchAsdos: function() {
      assistenServices.getAsisten().then((d) => {
        this.response = d.data;
        // TODO get asdos to this.response
      });
    },
  },
  components: {
    CreateAsisten,
  },
};
</script>

<style>
.title-asdos {
  margin-top: 50px;
  margin-bottom: 20px;
}
.create-asisten-div {
  margin-bottom: 20px;
  width: 60%;
}
.create-asisten-button {
  padding: 10px 20px;
  font-size: 13pt;
  font-weight: bolder;
  background: none;
  border-style: none;
  background-color: #FFDD00;
  border-radius: 1000px;
  text-decoration: none;
}
/* TABLE SECTION */
.table-div {
  width: 60%;
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
.remove-button {
  background: none;
  border-style: solid;
  font-weight: bolder;
  padding: 5px 10px;
  color: white;
  border-color: red;
  background-color: red;
  border-radius: 1000px;
}
.remove-button:hover {
  background-color: white;
  color: red;
}
</style>
