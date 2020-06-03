<template>
  <div id="unduh-karya-akhir">
    <div>
      <h2 class="title">
        Unduh Dokumen Kelengkapan
        <br>
        Sidang Karya Akhir
      </h2>

      <div class="menu-container">
        <div class="menu-unduh-list">
          <button v-for="surat in surat_karya_akhir"
            class="btn unduh-item" :key="surat.nama"
            @click="goToPage(surat.link)">
            {{ surat.nama }}
          </button>
        </div>

        <div class="button-container">
          <button id="edit-data" class="btn btn-yellow"
            @click="goToPage('sidang-akhir')">
            Ubah Data
          </button>

          <button id="unduh-semua" class="btn btn-yellow"
            @click="savePdf()">
            Print Semua
          </button>
        </div>
      </div>
    </div>
    <div id="document-to-print" class="display-none">
      <div class="pdf-viewer break-before" id="pdf-viewer">
        <div class="row">
          <div class="title-container">
            <h1>SURAT KETERANGAN</h1>
            <h1>KARYA AKHIR SIAP UJI</h1>
          </div>
        </div>
        <div class='row padding-top-50'>
          <p>Dengan ini disampaikan bahwa mahasiswa kami berikut:</p>
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
            Dengan pilihan Karya Akhir
          </div>
          <div class='col-40-px'>
            :
          </div>
          <div class='col-6'>
            {{ jenis_karya_akhir }}
          </div>
        </div>
        <div class='row padding-top-30 align-justify'>
          Telah kami setujui untuk diujikan dalam
          sebuah sidang karya akhir. Kepada Bidang
          Pendidikan, kami mohon dapat diproses evaluasi
          akhir studi dan surat persetujuan ujian sidang
          karya akhir kepada mahasiswa tersebut diatas.
        </div>
        <div class='row padding-top-30'>
          Judul karya akhir berbahasa Indonesia:
        </div>
        <div class='row align-justify'>
          {{ judul_karya_id }}
        </div>
        <div class='row padding-top-50'>
          Judul karya akhir berbahasa Inggris:
        </div>
        <div class='row align-justify'>
          {{ judul_karya_en }}
        </div>
        <div class='row align-left padding-top-50'>
          Tanda tangan Pengesahan:<br/>
        </div>
        <div class='row'>
          <div class='col-5'>
            <div class='row align-left'>
              Ketua Program Studi
            </div>
            <div class='row align-left'>
              Tanggal : . . . . . . . . . . . .
            </div>
          </div>
          <div class='col-5 align-top'>
            <div class='row align-right'>
              Pembimbing Karya Akhir,
            </div>
            <div class='row align-right'>
              Tanggal : . . . . . . . . . . . .
            </div>
            <div class='row align-right padding-top-80'>
              {{ pembimbing }}
            </div>
          </div>
        </div>
      </div>
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
            {{ ipk.toFixed(2) }}
          </div>
        </div>
        <div class='row'>
          Mengajukan permohonan dosen pembimbing untuk penulisan karya akhir
          yang akan saya buat dalam rangka penyelesaian studi saya di FEB UI.
          Adapun Karya Akhir yang akan saya buat adalah
          {{ jenis_karya_akhir.toLowerCase() }}
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
            <b>Bukan merupakan ujian kelulusan
            studi saya</b>, dan hanya merupakan
            ujian untuk mendapatkan nilai dari mata
            kuliah Karya Akhir.
          </div>
        </div>
        <div class='row-without-margin align-justify'>
          <div class='col-40-px align-top'>
            2.
          </div>
          <div class='col-9-3 align-justify'>
            Nilai dari mata kuliah Karya Akhir ini akan
            saya terima apabila saya
            telah menyerahkan semua perbaikan/revisi
            Karya Akhir yang diminta oleh
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
            di semester berikutnya, dan
            <b>saya tidak akan meminta dispensasi
            perbaikan nilai</b>
            atas mata kuliah yang tidak lulus tersebut
            dalam bentuk apapun.
          </div>
        </div>
        <div class='row-without-margin align-justify'>
          <div class='col-40-px align-top'>
            4.
          </div>
          <div class='col-9-3 align-justify'>
            Tanggal kelulusan bukan merupakan tanggal pelaksanaan ujian ataupun
            tanggal penyerahan revisi Karya Akhir saya, melainkan tanggal nilai
            masuk dari sisa mata kuliah yang terakhir di SIAK-NG.
          </div>
        </div>
        <div class='row align-justify padding-top-30'>
          Demikian surat pernyataan ini saya buat dengan penuh kesadaran,
          dan dengan data yang sebenar-benarnya. Saya tetap akan memenuhi
          semua ketentuan dan persyaratan akademis lain yang menjadi syarat
          kelulusan sarjana. Apabila di kemudian hari diketahui saya terbukti
          memberikan keterangan/data palsu (tidak benar), maka saya bersedia
          dikenakan sanksi akademis sebagaimana peraturan yang berlaku.
        </div>
        <div class='row align-center padding-top-50'>
          Depok, {{ date }}<br/>
        </div>
        <div class="padding-top-100 align-center">
          {{ nama }}<br/>
        </div>
      </div>
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
      <div class="pdf-viewer break-before" id="pdf-viewer">
        <div class="row">
          <div class="title-container">
            <h1>SURAT PERNYATAAN</h1>
          </div>
        </div>
        <div class='row padding-top-50'>
          <p>Dengan ini disampaikan bahwa mahasiswa kami berikut:</p>
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
          Menyatakan bahwa Karya Akhir yang saya tulis,
        </div>
        <div class='row'>
          Judul karya akhir berbahasa Indonesia:
        </div>
        <div class='row align-justify'>
          {{ judul_karya_id }}
        </div>
        <div class='row padding-top-50'>
          Judul karya akhir berbahasa Inggris:
        </div>
        <div class='row align-justify'>
          {{ judul_karya_en }}
        </div>
        <div class='row padding-top-50 align-justify'>
          Belum pernah dibuat sebelumnya oleh orang lain,
          baik judul maupun isinya.
        </div>
        <div class='row align-justify'>
          Sesuai tanda bukti pernyataan saya,
          bersama ini saya lampirkan daftar
          Karya Akhir yang pernah ditulis
          sebelumnya yang berhubungan dengan Karya
          Akhir saya. Data Karya Akhir ini adalah hasil kompilasi saya dari
          Perpustakaan Fakultas Ekonomi dan Bisnis Universitas Indonesia.
        </div>
        <div class='row align-justify'>
          Surat pernyataan ini saya buat dengan jujur dan
          dengan segala konsekuensinya.
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
</template>

<script>
import karyaAkhirApi from '@/services/karyaAkhirServices';

export default {
  name: 'UnduhDokumenKaryaAkhir',
  data() {
    return {
      surat_karya_akhir: [],
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
      ipk: '',
    };
  },
  created() {
    karyaAkhirApi.getMahasiswaProfile().then((d) => {
      const data = d.data['mahasiswa'];

      this.nama = data['nama'];
      this.npm = data['npm'];
      this.program_studi = data['program_studi'];
    });

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
          this.ipk = data['ipk'];
          this.fetchData();
        }).catch((e) => {
          if (e.response.status == 404) {
            this.isFormCompleted = false;
          }
        });
  },
  methods: {
    fetchData() {
      karyaAkhirApi.fetchDaftarSuratKaryaAkhir().then(
          (d) => {
            for (let i=0; i<d.data.surat_karya_akhir.length; i++) {
              this.$set(
                  this.surat_karya_akhir,
                  i,
                  d.data.surat_karya_akhir[i],
              );

              const namaSurat =
                this.surat_karya_akhir[i]['nama'].split(' ').join('-');
              this.surat_karya_akhir[i]['link'] = namaSurat.toLowerCase();
            }
          }
      );
    },
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
    savePdf: function() {
      window.print();
    },
    goToPage(name) {
      this.$router.push({name: name});
    },
  },
};
</script>

<style scoped>
.page-container {
  height: 100%;
  padding: 3%;
  box-sizing: border-box;
}
h2.title {
  font-family: 'Montserrat', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 27px;
  line-height: 40px;
  color: black;
  margin-top: 10px;
  text-align: center;
}
.menu-container {
  background: #2D3033;
  color: white;
  margin: 30px;
  padding: 10px 40px;
  border-radius: 18px;
  width: 380px;
  display: flex;
  flex-direction: column;
}
.menu-unduh-list {
  display: flex;
  flex-direction: column;
  margin: 8px 0;
}
.btn {
  cursor: pointer;
  word-break: break-word;
  border: 0;
  font-size: 15px;
}
.unduh-item {
  transition: 0s color;
  width: 100%;
  margin: 15px 0;
  background: #D8DADB;
  border-radius: 46.5px;
  padding: 9px 20px;
  font-weight: bold;
  line-height: 23px;
  color: black;
}
.btn-yellow {
  background: #FFDD00;
  border-radius: 60.5px;
}
.button-container {
  width: 100%;
  display: flex;
}
.button-container .btn {
  padding: 12px 25px;
  font-weight: bold;
  margin: 20px auto;
  width: 170px;
}

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

.padding-top-80 {
  padding-top: 80px;
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

h1 {
  font-size: 1.5em;
}

.align-top {
  vertical-align: top;
  height: 100%;
}

.col-5 {
  width: 50%;
  margin:0;
  padding:0;
  display: inline-block;
}

#table-ukab {
  width: 100%;
}

.display-none {
  display: none;
}

.margin-top-50 {
  margin-top: 50px;
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

  #document-to-print, #document-to-print * {
    visibility: visible !important;
  }

  #document-to-print {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
    display: block !important;
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
