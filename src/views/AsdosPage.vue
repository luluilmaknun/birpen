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

        <tr v-for="asisten in listAsdos" :key="asisten.username">
          <td id="username">
            {{ asisten.username }}
          </td>
          <td>
            <button
            class="remove-button"
            id="remove-btn"
            v-on:click="deleteAsdos(asisten.username)">
              Hapus
            </button>
          </td>
        </tr>
      </table>
    </div>

  </div>
</template>

<script>
import asistenServices from '@/services/asistenServices';
import CreateAsisten from '@/components/tambah-asisten';

export default {
  name: 'AsdosPage',
  data: function() {
    return {
      tableHead: [
        'User name', 'Aksi',
      ],
      listAsdos: [
        {
          'pk': 0,
          'username': 'athallah.annafis',
        },
        {
          'pk': 1,
          'username': 'ichlassul.affan',
        },
        {
          'pk': 2,
          'username': 'ahmad.fauzan',
        },
        {
          'pk': 3,
          'username': 'asdos',
        },
      ],
      response: {},
      listAsisten: [],
    };
  },
  created: function() {
    this.fetchAsdos();
  },
  methods: {
    fetchAsdos: function() {
      asistenServices.getAsisten().then((d) => {
        this.response = d.data;
        console.log(this.response);
        // TODO get asdos to this.response
        for (let i = 0; i < this.response.asisten_dosen.length; i++) {
            this.$set(this.listAsisten, i, this.response.asisten_dosen[i]);
        }
      });
    },
    deleteAsdos: function(name) {
      console.log(name);
      asistenServices.deleteAsisten({
        username: name,
      }).then((result) => {
        this.$router.go({
          path: '/asdos',
          force: true,
        });
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
