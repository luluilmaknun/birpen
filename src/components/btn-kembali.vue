<template>
  <div>
    <button class="yellow-black-btn" @click="back" id="back-btn">
      Kembali
    </button>
  </div>
</template>

<script>

export default {
  name: 'btn-kembali',
  methods: {
    back: function() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
.yellow-black-btn {
  background-color: #FFDD00;
  border-radius: 60.5px;
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 10pt;
  font-weight: bolder;
  border-style: solid;
  border-color: #FFDD00;
  cursor: pointer;
}

.yellow-black-btn:hover {
  background-color: white;
}
</style>
