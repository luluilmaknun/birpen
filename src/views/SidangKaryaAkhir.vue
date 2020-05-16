<template>
  <div>
    <h1>Mahasiswa Sidang Karya Akhir</h1>
    <div class="filter-div">
      <select aria-placeholder="Pilih Program Studi"
      v-model="programStudi">
        <option>Pilihan pertama</option>
        <option>Pilihan kedua</option>
        <option>Pilihan ketiga</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      programStudi: '',
    };
  },
}
</script>

<style scoped>

</style>