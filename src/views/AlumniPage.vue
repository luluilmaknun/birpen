<template>
  <div>
    <h1 class="title-alumni">
      Daftar Alumni
    </h1>

    <div id='loader_alumni'>
      <img src="../assets/icons/loader.svg"/>
    </div>

    <!-- TABLE SECTION -->
    <div id='alumni'>
    <div class="table-div">
      <table aria-hidden="true">
        <tr>
          <th id="table-header" class="head-table"
            v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="alumni in listAlumni" :key="alumni.username">
          <td id="username">
            {{ alumni.username }}
          </td>
          <td id="email">
              {{ alumni.email }}
          </td>
          <td id="status">
              <div v-if="alumni.blocked">Diblokir</div>
              <div v-else>Aktif</div>
          </td>
          <td>
            <ToggleBlockAlumni
            :alumni_username="alumni.username"
            :blocked="alumni.blocked"/>
          </td>
        </tr>
      </table>
    </div>
    </div>
  </div>
</template>

<script>
import alumniServices from '@/services/alumniServices';
import ToggleBlockAlumni from '@/components/toggle-block-alumni';

export default {
  name: 'AlumniPage',
  components: {
    ToggleBlockAlumni,
  },
  data() {
    return {
      tableHead: [
        'Username', 'Email', 'Status', 'Aksi',
      ],
      listAlumni: [],
      response: {},
    };
  },
  created() {
    this.fetchAlumni();
  },
  methods: {
    fetchAlumni() {
      alumniServices.fetchAlumni().then((result) => {
        this.response = result.data;

        for (let i = 0; i < this.response.alumni.length; i++) {
          this.$set(this.listAlumni, i, this.response.alumni[i]);
        }
      });
    },
  },
};
</script>

<style scoped>
#alumni {
  visibility: hidden;
}

.title-alumni {
  margin-top: 50px;
  margin-bottom: 20px;
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
  font-size: 15pt;
}
tr:nth-child(odd) {
  background-color: #D3D3D3;
}
td#username {
  word-break: break-all;
}
@media only screen and (max-width: 539px) {
  .table-div {
    width: 75%;
  }
}
</style>
