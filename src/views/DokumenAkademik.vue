<template>
  <div id="dokumen-akademik" class="page-container">
    <h2 class="title">Pemesanan Surat <br> Akademik </h2>
    <br>

    <div class="profile-container">
      <div class="input-row">
        <label>Nama: </label>
        <img v-if="isLoadProfile" src="@/assets/icons/loader-small.svg"/>
        <input v-else-if="isAlumni" class="profile-input"
          v-model="nama_pemesan">
        <span v-else class="">{{ nama_pemesan }}</span>
      </div>

      <div class="input-row">
        <label>NPM: </label>
        <img v-if="isLoadProfile" src="@/assets/icons/loader-small.svg"/>
        <input v-else-if="isAlumni" class="profile-input" v-model="npm_pemesan">
        <span v-else class="">{{ npm_pemesan }}</span>
      </div>
    </div>

    <!-- TABLE SECTION -->
    <table class="table-div" aria-hidden="true">
      <tr class="table-header">
        <th class="table-header-item" v-for="head in tableHead" :key="head"
          :class="head[0]" id="head[0]">
          {{ head[1] }}
        </th>
      </tr>

      <tr v-for="(item, id) in surat_akademik" :ref="'row_'+(id+1)" :key="item">
        <td class="no">
          {{ id+1 }}
        </td>
        <td class="jenis_dokumen">
          {{ item.jenis_dokumen }}
        </td>
        <td class="harga_satuan">
          <span v-if="isAlumni">{{ item.harga_alumni }}</span>
          <span v-else>{{ item.harga_mahasiswa }}</span>
        </td>
        <td class="jumlah">
          <div class="button-count-container">
            <button class="btn-count decrement"
              @click="update('decrement', id)">
              -
            </button>
            <input type="number" :ref="'jumlah_' + (id+1)"
              class="jumlah_surat" value=0 min=0 >
            <button class="btn-count increment"
              @click="update('increment', id)">
              +
            </button>
          </div>
        </td>
      </tr>
    </table>

    <br>
    <br>
    <div class="button-container pemesanan" v-if="!isLoadTableDoc">
      <button @click="summarize">Pesan</button>
      <button @click="goToPage('surat')">Kembali</button>
    </div>

    <div v-if="isLoadTableDoc">
      <img src="@/assets/icons/loader.svg"/>
    </div>

    <modal name="ringkasan" height="auto" :pivotX="0.0" :width="1000">
      <div class="modal-container">
        <RingkasanPemesanan :surat_akademik="pesanan"
           :list_harga="list_harga" :jumlah_harga="jumlah_harga" />
        <span class="text-danger">{{ error_message }}</span>
        <div class="button-container ringkasan">
          <button class="btn btn-grn" @click="validateData">
            Pesan
          </button>

          <button class="btn btn-red" @click="closeModal('ringkasan')">
            Batal
          </button>
        </div>
      </div>
    </modal>
  </div>
</template>

<script>
import suratApi from '@/services/suratServices';
import RingkasanPemesanan from '@/components/ringkasan-pemesanan';

export default {
  name: 'DokumenAkademik',
  components: {
    RingkasanPemesanan,
  },
  data: function() {
    return {
      isAlumni: localStorage['role'] == 'alumni',
      tableHead: [
        ['no', 'No'],
        ['jenis_dokumen', 'Jenis Dokumen'],
        ['harga_satuan', 'Harga Satuan'],
        ['jumlah', 'Jumlah'],
      ],
      error_message: '',
      nama_pemesan: '',
      npm_pemesan: '',
      jumlah_harga: 0,
      surat_akademik: [],
      pesanan: [],
      list_harga: {},
      temp_pesanan: {},
      response: {},
      isLoadProfile: false,
      isLoadTableDoc: false,
    };
  },
  created() {
    this.fetchLetterList();

    if (!this.isAlumni) {
      this.isLoadProfile = true;
      suratApi.fetchDataPemesan().then((d) => {
        this.isLoadProfile = false;
        this.nama_pemesan = d.data.mahasiswa.nama;
        this.npm_pemesan = d.data.mahasiswa.npm;
      });
    }
  },
  methods: {
    fetchLetterList() {
      this.isLoadTableDoc = true,
      suratApi.fetchSuratAkademik().then((d) => {
        this.isLoadTableDoc = false,
        this.response = d.data.surat_akademik;

        for (let i = 0; i < this.response.length; i++) {
          this.$set(this.surat_akademik, i, this.response[i]);
        }
      });
    },
    update(type, id) {
      const inputId = 'jumlah_' + (id+1);
      const input = this.$refs[inputId][0];
      const currValue = parseInt(input.value);

      if (type == 'increment') {
        input.value = currValue + 1;
      } else if (type == 'decrement') {
        // Check for minimum value zero
        if (currValue == 0) {
          input.value = 0;
        } else {
          input.value = currValue - 1;
        }
      }

      this.updatePesanan(id);
    },
    updatePesanan(id) {
      const rowId = 'row_' + (id+1);
      const inputId = 'jumlah_' + (id+1);
      const row = this.$refs[rowId][0];
      const input = this.$refs[inputId][0];

      const jenisDokumen = row.childNodes[1].innerText;
      const harga = row.childNodes[2].innerText;
      const jumlah = input.value;

      this.temp_pesanan[jenisDokumen] = {};
      this.temp_pesanan[jenisDokumen]['jumlah'] = jumlah;
      this.temp_pesanan[jenisDokumen]['harga'] = harga;
    },
    showModal(name) {
      this.$modal.show(name);
    },
    closeModal(name) {
      this.error_message= '';
      this.$modal.hide(name);
    },
    goToPage(path) {
      this.$router.push({name: path});
    },
    validateData() {
      if (this.nama_pemesan == '' || this.npm_pemesan == '') {
        this.error_message = 'Nama dan NPM belum diisi';
      } else if (this.pesanan.length == 0) {
        this.error_message = 'Silahkan pilih pesanan terlebih dahulu';
      } else {
        this.requestLetter();
      }
    },
    summarize() {
      this.jumlah_harga = 0;
      this.pesanan = [];
      this.error_message= '';

      for (const k in this.temp_pesanan) {
        if (this.temp_pesanan.hasOwnProperty(k)) {
          const jumlah = parseInt(this.temp_pesanan[k]['jumlah']);

          if (!jumlah == 0) {
            const hargaSatuan = parseInt(this.temp_pesanan[k]['harga']);
            const harga = jumlah * hargaSatuan;

            this.pesanan.push({
              'jenis_dokumen': k,
              'jumlah': jumlah,
            });

            this.jumlah_harga = this.jumlah_harga + harga;
            this.list_harga[k] = this.temp_pesanan[k]['harga'];
          }
        }
      }

      this.showModal('ringkasan');
    },
    requestLetter() {
      const request = {};

      if (this.isAlumni) {
        request['nama_pemesan'] = this.nama_pemesan;
        request['npm_pemesan'] = this.npm_pemesan;
      }
      request['surat_akademik'] = this.pesanan;

      suratApi.createPesanan(request).then((d) => {
        this.error_message= '';
        this.$router.push({name: 'tracking-surat'});
      }).catch((error) => {
        this.error_message = error.response.data.detail;
      });
    },
  },
};
</script>

<style scoped>
button {
  cursor: pointer;
}
#dokumen-akademik.page-container {
  padding: 3% 8%;
}
#dokumen-akademik .title {
  font-weight: 700;
  font-size: 40px;
  line-height: 45px;
  text-align: center;
  color: #000;
}
.profile-container {
  padding: 30px;
  margin-left: 10px;
  font-size: 18px;
}
.profile-container .input-row {
  margin: 20px;
}
.profile-container .input-row label {
  width: 100px;
  display: inline-block;
}
.profile-container .input-row span {
  font-weight: 700;
  display: inline-block;
}
.profile-container input {
  height: 25px;
  border-radius: 7px;
  border: 1px solid black;
  width: 250px;
  padding: 6px;
  font-weight: 700;
}
table.table-div {
  width: 100%;
  border: 1.5px solid black;
  border-radius: 1em;
  border-spacing: 0;
}
th:first-of-type {
  border-top-left-radius: 10px;
}
th:last-of-type {
  border-top-right-radius: 10px;
}
th {
  background-color: black;
  padding: 13px;
  color: white;
  font-weight: 700;
}
td {
  padding: 13px;
  border-bottom: .5px solid black;
  word-break: break-word;
}
tr:last-of-type td {
  border-bottom: 0;
}
th.no, td.no {
  width: 5%;
  text-align: center;
}
th.jenis_dokumen, td.jenis_dokumen {
  width: 65%;
  text-align: left;
}
th.harga_satuan, td.harga_satuan {
  width: 15%;
  text-align: center;
}
th.jumlah, td.jumlah {
  width: 15%;
  min-width: 85px;
  text-align: center;
}
button.btn-count {
  border: 0;
  background-color: #FFDD00;
  color: black;
  padding: 7px 10px;
}
button.btn-count.increment {
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}
button.btn-count.decrement {
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}
input.jumlah_surat {
  width: 40px;
  border: 0;
  text-align: center;
  padding: 0;
}
input[type='number'] {
    -moz-appearance:textfield;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}
.button-container.pemesanan {
  margin-right: 50px;
}
.button-container.pemesanan button {
  border: 0;
  border-radius: 30px;
  background-color: #D8DADB;
  color: black;
  font-weight: 700;
  margin: 20px;
  padding: 15px;
  min-width: 150px;
}
.button-container.pemesanan button:hover {
  background-color: #FFDD00;
  color: black;
}
.text-danger {
  color: red;
  font-weight: 700;
}
.button-container.ringkasan {
  margin: 10px auto;
  text-align: center;
}
.button-container.ringkasan .btn {
  font-size: 23px;
  font-weight: bolder;
  padding: 8px 30px;
  width: 135px;
  border-radius: 34.5px;
  margin: 15px;
}
.button-container.ringkasan .btn-grn:hover {
  background-color: white;
  color: #3C8F2F;
}
.button-container.ringkasan .btn-red:hover {
  background-color: white;
  color: #E63946;
}
.button-container.ringkasan .btn-grn {
  border: 2px solid #3C8F2F;
  background: #3C8F2F;
  color: white;
}
.button-container.ringkasan .btn-red {
  border: 2px solid #E63946;
  background: #E63946;
  color: white;
}
</style>
