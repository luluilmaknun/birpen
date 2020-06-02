<template>
  <div>
    <h1 class="title-admin">
      Daftar Admin
    </h1>

    <div class="create-admin-container">
      <CreateAdmin/>
    </div>

    <!-- TABLE SECTION -->
    <div class="table-div">
      <table aria-hidden="true">
        <tr>
          <th id="table-header" class="head-table"
            v-for="head in tableHead" :key="head">
            {{ head }}
          </th>
        </tr>

        <tr v-for="admin in listAdmin" :key="admin.username">
          <td id="username">
            {{ admin.username }}
          </td>
          <td>
            <DeleteAdmin :deleted_admin_username="admin.username"/>
          </td>
        </tr>
      </table>

      <div v-if="isLoadAdminTable">
        <img src="@/assets/icons/loader.svg"/>
      </div>

    </div>
  </div>
</template>

<script>
import adminApi from '@/services/adminServices';
import CreateAdmin from '@/components/tambah-admin';
import DeleteAdmin from '@/components/delete-admin';

export default {
  name: 'AdminPage',
  components: {
    CreateAdmin,
    DeleteAdmin,
  },
  data() {
    return {
      tableHead: [
        'Username', 'Aksi',
      ],
      response: {},
      listAdmin: [],
      isLoadAdminTable: false,
    };
  },
  created() {
    this.fetchAdmin();
  },
  methods: {
    fetchAdmin() {
      this.isLoadAdminTable = true;
      adminApi.fetchAdmin().then((d) => {
        this.isLoadAdminTable = false;
        this.response = d.data;

        for (let i = 0; i < this.response.admin.length; i++) {
          this.$set(this.listAdmin, i, this.response.admin[i]);
        }
      });
    },
  },
};
</script>

<style scoped>
.title-admin {
  margin-top: 50px;
  margin-bottom: 20px;
}
.create-admin-container {
  margin-bottom: 20px;
  width: 60%;
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
