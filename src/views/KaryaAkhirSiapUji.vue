<template>
  <div class="KaryaAkhirSiapUji">
    <div class="title-container">
      <h1>Surat Keterangan Karya<br>Akhir Siap Uji</h1>
    </div>
    <div class="pdf-viewer">
      <!-- TODO -->
    </div>
    <div class="bot-container">
      <SaveBtn id="btn" link_download="TODO"/>
      <BackBtn id="btn" />
    </div>
  </div>
</template>

<script>
import BackBtn from '@/components/btn-kembali';
import SaveBtn from '@/components/btn-simpan';

export default {
  name: 'KaryaAkhirSiapUji',
  components: {BackBtn, SaveBtn},
};
</script>

<style scoped>
.title-container {
  text-align: center;
  margin: 20px;
}

.bot-container {
  display: flex;
  flex-direction: row;
  margin: 20px;
}

.bot-container #btn {
  margin: 30px;
}
</style>
