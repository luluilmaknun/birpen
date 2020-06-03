<template>
  <div v-if="isGetMahasiswaProfile || isReadDataKaryaAkhir">
    <img src="@/assets/icons/loader.svg"/>
  </div>
  <div v-else class="PenunjukkanDospem">
    <div class="container">
      <div id="display-print"> <!-- Start of display -->
        <div class="border">
          <div class="pdf-viewer break-before" id="pdf-viewer">
            <div class="row">
              <div class="title-container">
                <h1>FORMULIR</h1>
                <h1>PENUNJUKKAN DOSEN PEMBIMBING</h1>
                <h1>KARYA AKHIR - MAHASISWA S1 REGULER</h1>
              </div>
            </div>
            <div class='row padding-top-50'>
              <b>Kepada Yth.</b><br/>
              <b>{{ pembimbing }}</b><br/>
              <b>Di tempat</b><br/>
            </div>
            <div class='row'>
              Dengan ini kami menugaskan Saudara sebagai dosen pembimbing dalam
              Karya Akhir mahasiswa
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
              Demikian surat penunjukkan ini kami buat,
              bimbingan atas mahasiswa tersebut kami serahkan
              sepenuhnya kepada Saudara.
            </div>
            <div class='row align-right padding-top-50'>
              Depok, {{ date }}<br/>
            </div>
            <div class='row padding-top-30'>
              <div class='col-5'>
                <div class='row align-left'>
                  Penerima Tugas,<br/>
                  Dosen Pembimbing,<br/>
                </div>
                <div class='row align-left padding-top-80'>
                  {{ pembimbing }}
                </div>
              </div>
              <div class='col-5 align-top'>
                <div class='row align-right'>
                  Pemberi Tugas,<br/>
                  Ketua Program Studi,<br/>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="border margin-top-50"
          v-if="pembimbing_pendamping != null
          && pembimbing_pendamping.length > 1">
          <div
            class="pdf-viewer break-before" id="pdf-viewer">
            <div class="row">
              <div class="title-container">
                <h1>FORMULIR</h1>
                <h1>PENUNJUKKAN DOSEN PEMBIMBING</h1>
                <h1>KARYA AKHIR - MAHASISWA S1 REGULER</h1>
              </div>
            </div>
            <div class='row padding-top-50'>
              <b>Kepada Yth.</b><br/>
              <b>{{ pembimbing_pendamping }}</b><br/>
              <b>Di tempat</b><br/>
            </div>
            <div class='row'>
              Dengan ini kami menugaskan Saudara sebagai dosen pembimbing dalam
              Karya Akhir mahasiswa
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
              Demikian surat penunjukkan ini kami buat,
              bimbingan atas mahasiswa tersebut kami serahkan
              sepenuhnya kepada Saudara.
            </div>
            <div class='row align-right padding-top-50'>
              Depok, {{ date }}<br/>
            </div>
            <div class='row padding-top-30'>
              <div class='col-5'>
                <div class='row align-left'>
                  Penerima Tugas,<br/>
                  Dosen Pembimbing,<br/>
                </div>
                <div class='row align-left padding-top-80'>
                  {{ pembimbing_pendamping }}
                </div>
              </div>
              <div class='col-5 align-top'>
                <div class='row align-right'>
                  Pemberi Tugas,<br/>
                  Ketua Program Studi,<br/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div><!-- End of display -->
      <div id="print" class="display-none"> <!-- Start of print -->
        <div class="pdf-viewer break-before" id="pdf-viewer">
          <div class="row">
            <div class="title-container">
              <h1>FORMULIR</h1>
              <h1>PENUNJUKKAN DOSEN PEMBIMBING</h1>
              <h1>KARYA AKHIR - MAHASISWA S1 REGULER</h1>
            </div>
          </div>
          <div class='row padding-top-50'>
            <b>Kepada Yth.</b><br/>
            <b>{{ pembimbing }}</b><br/>
            <b>Di tempat</b><br/>
          </div>
          <div class='row'>
            Dengan ini kami menugaskan Saudara sebagai dosen pembimbing dalam
            Karya Akhir mahasiswa
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
            Demikian surat penunjukkan ini kami buat,
            bimbingan atas mahasiswa tersebut kami serahkan
            sepenuhnya kepada Saudara.
          </div>
          <div class='row align-right padding-top-50'>
            Depok, {{ date }}<br/>
          </div>
          <div class='row padding-top-30'>
            <div class='col-5'>
              <div class='row align-left'>
                Penerima Tugas,<br/>
                Dosen Pembimbing,<br/>
              </div>
              <div class='row align-left padding-top-80'>
                {{ pembimbing }}
              </div>
            </div>
            <div class='col-5 align-top'>
              <div class='row align-right'>
                Pemberi Tugas,<br/>
                Ketua Program Studi,<br/>
              </div>
            </div>
          </div>
        </div>
        <div v-if="pembimbing_pendamping != null
        && pembimbing_pendamping.length > 0"
          class="pdf-viewer break-before" id="pdf-viewer">
          <div class="row">
            <div class="title-container">
              <h1>FORMULIR</h1>
              <h1>PENUNJUKKAN DOSEN PEMBIMBING</h1>
              <h1>KARYA AKHIR - MAHASISWA S1 REGULER</h1>
            </div>
          </div>
          <div class='row padding-top-50'>
            <b>Kepada Yth.</b><br/>
            <b>{{ pembimbing_pendamping }}</b><br/>
            <b>Di tempat</b><br/>
          </div>
          <div class='row'>
            Dengan ini kami menugaskan Saudara sebagai dosen pembimbing dalam
            Karya Akhir mahasiswa
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
            Demikian surat penunjukkan ini kami buat,
            bimbingan atas mahasiswa tersebut kami serahkan
            sepenuhnya kepada Saudara.
          </div>
          <div class='row align-right padding-top-50'>
            Depok, {{ date }}<br/>
          </div>
          <div class='row padding-top-30'>
            <div class='col-5'>
              <div class='row align-left'>
                Penerima Tugas,<br/>
                Dosen Pembimbing,<br/>
              </div>
              <div class='row align-left padding-top-80'>
                {{ pembimbing_pendamping }}
              </div>
            </div>
            <div class='col-5 align-top'>
              <div class='row align-right'>
                Pemberi Tugas,<br/>
                Ketua Program Studi,<br/>
              </div>
            </div>
          </div>
        </div>
      </div> <!-- End of print -->
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
  name: 'PenunjukkanDospem',
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
      isGetMahasiswaProfile: false,
      isReadDataKaryaAkhir: false,
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

      this.isReadDataKaryaAkhir = true;
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
            this.isReadDataKaryaAkhir = false;
          });
      
      this.isGetMahasiswaProfile = true;
      karyaAkhirApi.getMahasiswaProfile().then((d) => {
        const data = d.data['mahasiswa'];

        this.nama = data['nama'];
        this.npm = data['npm'];
        this.program_studi = data['program_studi'];
        this.isGetMahasiswaProfile = false;
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

.col-5 {
  width: 50%;
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

.padding-top-80 {
  padding-top: 80px;
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

.align-top {
  vertical-align: top;
  height: 100%;
}

h1 {
  font-size: 1.5em;
}

.display-none {
  display: none;
}

.margin-top-50 {
  margin-top: 50px;
}
</style>
