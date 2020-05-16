<template>
  <div>
    <h1>Mahasiswa Sidang Karya Akhir</h1>
    <div class="main-container">
      <div class="filter-div">
        <select class="filter-element" id="studi-choices" v-model="chosenStudi">
          <option :value="''" hidden>Pilih Program Studi</option>
          <option v-for="studi in programStudiDummy"
          :key="studi.pk"
          :value="studi.nama">
            {{ studi.nama }}
          </option>
        </select>
        <input placeholder="Tulis nama angkatan"
        class="filter-element" id="angkatan-input" v-model="angkatan"/>
      </div>
    </div>
  </div>
</template>

<script>
import apiSidangAkhir from '@/services/sidangKaryaAkhirServices.js';
export default {
  data: function() {
    return {
      angkatan: '',
      chosenStudi: '',
      programStudiDummy: [
        {
          pk: 1,
          nama: 'Manajemen'
        },
        {
          pk: 2,
          nama: 'Akuntansi'
        },
        {
          pk: 3,
          nama: 'Bisnis Islam'
        },
        {
          pk: 4,
          nama: 'Ilmu Ekonomi Islam'
        },
      ],
      programStudiResponse: {},
    };
  },
  created: function() {
    this.fetchProgramStudi();
  },
  methods: {
    fetchProgramStudi: function() {
      apiSidangAkhir.getProgramStudi().then((result) => {
        this.programStudiResponse = result.data;
      })
    }
  },
}
</script>

<style scoped>
.filter-div {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
}
.filter-element {
  text-align: center;
  width: 200px;
  background: none;
  border-style: solid;
  border-width: 2px;
  border-color: black;
  background-color: white;
  border-radius: 10px;
  padding: 10px 10px;
}
</style>