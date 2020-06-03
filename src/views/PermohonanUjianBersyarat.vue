<template>
  <div class="PermohonanUjianBersyarat">
    <div class="container">
      <div class="border">
        <div id="print">
          <div class="pdf-viewer break-before" id="pdf-viewer">
            <div class="row">
              <div class="title-container">
                <h1>SURAT PERMOHONAN MENGIKUTI</h1>
                <h1>UJIAN KARYA AKHIR BERSYARAT (UKAB)</h1>
              </div>
            </div>
            <div class='row-bottom-5'>
              <p>Saya yang bertandatangan di bawah ini:</p>
            </div>
            <div class='row-bottom-5'>
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
            <div class='row-bottom-5'>
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
            <div class='row-bottom-5'>
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
                Jenis Karya Akhir
              </div>
              <div class='col-40-px'>
                :
              </div>
              <div class='col-6'>
                {{ jenis_karya_akhir }}
              </div>
            </div>
            <div class='row align-justify'>
              Dengan ini menyatakan dengan sebenar-benarnya bahwa Karya
              Akhir yang telah saya buat telah dinyatakan <b>LAYAK UJI</b>
              oleh Pembimbing saya. Sehubungan dengan hal tersebut, dengan
              ini saya mengajukan permohonan ijin untuk melaksanakan ujian
              mata kuliah Karya Akhir terlebih dahulu sebelum keluarnya
              nilai dari mata kuliah berikut ini:<br/>
              <img id="table-ukab" src="@/assets/images/table-ukab.png">
            </div>
            <div class='row-without-margin align-justify'>
              Saya mengetahui, menyetujui, dan akan melaksanakan dengan
              sebenar-benarnya secara konsekuen, bahwa atas permohonan UKAB ini:
            </div>
            <div class='row-without-margin align-justify'>
              <div class='col-40-px align-top'>
                1.
              </div>
              <div class='col-9-3 align-justify'>
                <b>Bukan merupakan ujian kelulusan studi saya</b>,
                dan hanya merupakan ujian untuk mendapatkan nilai
                dari mata kuliah Karya Akhir.
              </div>
            </div>
            <div class='row-without-margin align-justify'>
              <div class='col-40-px align-top'>
                2.
              </div>
              <div class='col-9-3 align-justify'>
                Nilai dari mata kuliah Karya Akhir ini akan saya
                terima apabila saya telah menyerahkan semua
                perbaikan/revisi Karya Akhir yang diminta oleh
                Tim Penguji secara tepat waktu.
              </div>
            </div>
            <div class='row-without-margin align-justify'>
              <div class='col-40-px align-top'>
                3.
              </div>
              <div class='col-9-3 align-justify'>
                Apabila terdapat mata kuliah tersebut diatas
                yang tidak lulus, maka saya
                <b>berkewajiban untuk mengulangnya hingga lulus</b>
                di semester berikutnya, dan <b>saya tidak akan
                meminta dispensasi perbaikan nilai</b> atas mata
                kuliah yang tidak lulus tersebut
                dalam bentuk apapun.
              </div>
            </div>
            <div class='row-without-margin align-justify'>
              <div class='col-40-px align-top'>
                4.
              </div>
              <div class='col-9-3 align-justify'>
                Tanggal kelulusan bukan merupakan tanggal
                pelaksanaan ujian ataupun tanggal penyerahan
                revisi Karya Akhir saya, melainkan tanggal nilai
                masuk dari sisa mata kuliah yang terakhir di SIAK-NG.
              </div>
            </div>
            <div class='row align-justify padding-top-30'>
              Demikian surat pernyataan ini saya buat dengan penuh kesadaran,
              dan dengan data yang sebenar-benarnya. Saya tetap akan memenuhi
              semua ketentuan dan persyaratan akademis lain yang menjadi syarat
              kelulusan sarjana. Apabila di kemudian hari diketahui
              saya terbukti memberikan keterangan/data palsu
              (tidak benar), maka saya bersedia
              dikenakan sanksi akademis sebagaimana peraturan yang berlaku.
            </div>
            <div class='row align-center padding-top-50'>
              Depok, {{ date }}<br/>
            </div>
            <div class="padding-top-100 align-center">
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
  name: 'PermohonanUjianBersyarat',
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
      this.date = today.getDate()
                  + ' '
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

.row-bottom-5 {
  display: inline-block;
  width: 100%;
  margin-bottom: 5px;
}

.row-without-margin {
  display: inline-block;
  width: 100%;
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

.col-9-3 {
  width: 93%;
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

.align-center {
  text-align: center;
}

.align-justify {
  text-align: justify;
}

.align-top {
  vertical-align: top;
  height: 100%;
}

#table-ukab {
  width: 100%;
}

h1 {
  font-size: 1.5em;
}
</style>
