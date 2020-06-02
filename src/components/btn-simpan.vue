<template>
  <div>
    <button class="yellow-black-btn" @click="savePdf()">
      <a>Print</a>
    </button>
  </div>
</template>

<script>

export default {
  name: 'btn-simpan',
  methods: {
    savePdf: function() {
      window.print();
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

#link {
  text-decoration: none;
  color: black;
}
</style>

<style>
@media print {
  body * {
    visibility: hidden !important;
    float: none !important;
  }
  div {
    float: none;
  }
  #print, #print * {
    visibility: visible !important;
  }
  #print {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
  }
  .break-after {
    display: block !important;
    page-break-after: always !important;
    position: relative !important;
    page-break-inside: avoid !important;
  }
  .break-before {
    display: block !important;
    page-break-before: always !important;
    position: relative !important;
    page-break-inside: avoid !important;
  }

  @page 
  {
      size: auto;   /* auto is the initial value */
      margin: 0mm;  /* this affects the margin in the printer settings */
  }
}
</style>