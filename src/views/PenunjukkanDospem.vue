<template>
  <div class="PenunjukkanDospem">
    <div class="title-container">
      <h1>Formulir Penunjukkan<br>Dosen Pembimbing</h1>
    </div>
    <div class="pdf-viewer">
      <!-- TODO -->
    </div>
    <div class="bot-container">
      <SaveBtn id="btn" />
      <BackBtn id="btn" />
    </div>
  </div>
</template>

<script>
import BackBtn from '@/components/btn-kembali';
import SaveBtn from '@/components/btn-simpan';

export default {
  name: 'PenunjukkanDospem',
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
