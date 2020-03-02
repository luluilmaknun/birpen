<template>
  <div>
    <date-pick
      v-model="date"
      :inputAttributes="{readonly: true}"
      :displayFormat="'DD-MM-YYYY'">
    </date-pick>
  </div>
</template>

<script>
import DatePick from 'vue-date-pick';
import 'vue-date-pick/dist/vueDatePick.css';

export default {
  components: {DatePick},
  data: () => ({
    date: '',
  }),
};
</script>
