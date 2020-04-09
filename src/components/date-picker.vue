<template>
  <div>
    <div class="container">
      <date-pick
          v-model="date"
          :inputAttributes="{readonly: true}"
          :isDateDisabled="isFutureDate"
          :format="'DD-MM-YYYY'"
      ></date-pick>
      <div v-show="show">
      </div>
      <button>
        <a :href="'/pengumuman/?tanggal='+date">Filter</a>
      </button>
    </div>
  </div>
</template>

<script>
import DatePick from 'vue-date-pick';
import 'vue-date-pick/dist/vueDatePick.css';

export default {
  components: {DatePick},
  data: function() {
    return {
      date: '',
      show: false,
    };
  },
};
</script>

<style>
 .container {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.container a {
  text-decoration: none;
  color:black;
}
</style>


