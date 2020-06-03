<template>
  <div class="PengajuanDospem">
    <div class="container">
      <div class="border">
        <div id="print">
          <div class="pdf-viewer break-before" id="pdf-viewer">
            <div class="row">
              <div class="title-container">
                <h1>FORM PENGAJUAN</h1>
                <h1>DOSEN PEMBIMBING KARYA AKHIR</h1>
              </div>
            </div>
            <div class='row padding-top-50'>
              <b>Kepada Yth.</b><br/>
              <b>Ketua Program Studi</b><br/><br/><br/>
              <b>Di tempat</b><br/>
            </div>
            <div class='row padding-top-30'>
              <p>Dengan ini saya:</p>
            </div>
            <div class='row'>
              <div class='col-3'>
                Nama
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ nama }}
              </div>
            </div>
            <div class='row'>
              <div class='col-3'>
                Nomor Pokok Mahasiswa
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ npm }}
              </div>
            </div>
            <div class='row'>
              <div class='col-3'>
                Program Studi
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ program_studi }}
              </div>
            </div>
            <div class='row'>
              <div class='col-3'>
                Konsentrasi
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ peminatan_mahasiswa }}
              </div>
            </div>
            <div class='row'>
              <div class='col-3'>
                Jumlah SKS diperoleh
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ sks_diperoleh }}
              </div>
            </div>
            <div class='row'>
              <div class='col-3'>
                IPK
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
              </div>
            </div>
            <div class='row'>
              Mengajukan permohonan dosen pembimbing untuk
              penulisan karya akhir yang akan saya buat
              dalam rangka penyelesaian studi saya di FEB UI.
              Adapun Karya Akhir yang akan saya buat
              adalah {{ jenis_karya_akhir.toLowerCase() }}
            </div>
            <div class='row'>
              Dengan judul topik:
            </div>
            <div class='row align-justify'>
              {{ judul_karya_id }}
            </div>
            <div class='row padding-top-50 align-justify'>
              Demikian surat permohonan ini saya buat, atas perhatiannya
              saya ucapkan terima kasih.
            </div>
            <div class='row align-right padding-top-30'>
              Depok, {{ date }}<br/>
              Yang membuat pernyataan,<br/>
            </div>
            <div class="padding-top-100 align-right">
              {{ nama }}<br/>
            </div>
          </div>
        </div>
      </div>
      <div class="bot-container">
        <SaveBtn id="btn" link_download="TODO"/>
        <BackBtn id="btn" />
      </div>
    </div>
  </div>
</template>

<script>
import BackBtn from '@/components/btn-kembali';
import SaveBtn from '@/components/btn-simpan';
import karyaAkhirApi from '@/services/karyaAkhirServices';

export default {
  name: 'PengajuanDospem',
  components: {BackBtn, SaveBtn},
  data: function() {
    return {
      nama: '',
      npm: '',
      program_studi: '',
      peminatan_mahasiswa: '',
      jenis_karya_akhir: '',
      sks_diperoleh: '',
      pembimbing: '',
      pembimbing_pendamping: '',
      judul_karya_id: '',
      judul_karya_en: '',
      tanggal: '',
    };
  },
  methods: {
    translateMonth(number) {
      let month = '';
      if (number == 1) {
        month = 'Januari';
      } else if (number == 2) {
        month = 'Februari';
      } else if (number == 3) {
        month = 'Maret';
      } else if (number == 4) {
        month = 'April';
      } else if (number == 5) {
        month = 'Mei';
      } else if (number == 6) {
        month = 'Juni';
      } else if (number == 7) {
        month = 'Juli';
      } else if (number == 8) {
        month = 'Agustus';
      } else if (number == 9) {
        month = 'September';
      } else if (number == 10) {
        month = 'Oktober';
      } else if (number == 11) {
        month = 'November';
      } else if (number == 12) {
        month = 'Desember';
      }
      return month;
    },
    fetchData() {
      const today = new Date();
      this.date = today.getDate() + ' '
                  + this.translateMonth(today.getMonth()+1)
                  + ' ' + today.getFullYear();

      karyaAkhirApi.readDataKaryaAkhir(localStorage.getItem('username'))
          .then((d) => {
            const data = d.data['data_karya_akhir'];

            this.peminatan_mahasiswa = data['peminatan_mahasiswa'];
            this.jenis_karya_akhir = data['jenis_karya_akhir'];
            this.sks_diperoleh = parseInt(data['sks_diperoleh']);
            this.pembimbing = data['pembimbing'];
            this.pembimbing_pendamping = data['pembimbing_pendamping'];
            this.judul_karya_id = data['judul_karya_id'];
            this.judul_karya_en = data['judul_karya_en'];
          });

      karyaAkhirApi.getMahasiswaProfile().then((d) => {
        const data = d.data['mahasiswa'];

        this.nama = data['nama'];
        this.npm = data['npm'];
        this.program_studi = data['program_studi'];
      });
    },
  },
  created: function() {
    this.fetchData();
  },
};
</script>

<style scoped>

.row {
  display: inline-block;
  width: 100%;
  margin-bottom: 20px;
}

.col-40-px {
  width: 40px;
  margin:0;
  padding:0;
  display: inline-block;
}

.col-3 {
  width: 30%;
  margin:0;
  padding:0;
  display: inline-block;
}

.col-6 {
  width: 63%;
  margin:0;
  padding:0;
  display: inline-block;
}

.container {
  margin-top: 80px;
  padding: 10px;
  display: block;
}

.title-container {
  text-align: center;
}

.bot-container {
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-right: 30%;
  margin-left: 30%;
}

.bot-container #btn {
  margin: 30px;
}

.pdf-viewer {
  width: 794px;
  height: 1123px;
  padding: 96px;
}

.pdf-viewer * {
  font-family: Arial, Helvetica, sans-serif;
}

.border {
  border-style: solid;
  border-color: black;
}

.padding-top-100 {
  padding-top: 100px;
}

.padding-top-50 {
  padding-top: 50px;
}

.padding-top-30 {
  padding-top: 30px;
}

.align-right {
  text-align: right;
}

.align-justify {
  text-align: justify;
}

h1 {
  font-size: 1.5em;
}
</style>
