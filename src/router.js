import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Home.vue';
import Login from '@/views/Login.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import EditAnnouncement from '@/views/EditAnnouncement.vue';
import AsdosPage from '@/views/AsdosPage.vue';
import Pengumuman from '@/views/Pengumuman.vue';
import MainMenuSurat from '@/views/MainMenuSurat.vue';
import AdminPage from '@/views/AdminPage.vue';
import Register from '@/views/Register.vue';
import AlumniPage from '@/views/AlumniPage.vue';
import DetailPengajuanSurat from '@/views/DetailPengajuanSurat.vue';
import TrackingPesanan from '@/views/TrackingPesanan.vue';
import DokumenAkademik from '@/views/DokumenAkademik.vue';
import KaryaAkhirSiapUji from '@/views/KaryaAkhirSiapUji';
import PengajuanDospem from '@/views/PengajuanDospem';
import PenunjukkanDospem from '@/views/PenunjukkanDospem';
import PermohonanUjianBersyarat from '@/views/PermohonanUjianBersyarat';
import SuratPernyataan from '@/views/SuratPernyataan';
import UnduhDokumenKaryaAkhir from '@/views/UnduhDokumenKaryaAkhir.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/surat/',
      name: 'surat',
      component: MainMenuSurat,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/surat/sidang/',
      name: 'sidang-akhir',
      component: null,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/unduh/',
      name: 'unduh-dokumen-karya-akhir',
      component: UnduhDokumenKaryaAkhir,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/surat-karya-akhir-siap-uji/',
      name: 'surat-karya-akhir-siap-uji',
      component: KaryaAkhirSiapUji,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/form-pengajuan-dosen-pembimbing-karya-akhir/',
      name: 'form-pengajuan-dosen-pembimbing-karya-akhir',
      component: PengajuanDospem,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/form-penunjukkan-dosen-pembimbing/',
      name: 'form-penunjukkan-dosen-pembimbing',
      component: PenunjukkanDospem,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/surat-pernyataan/',
      name: 'surat-pernyataan',
      component: SuratPernyataan,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/sidang/surat-permohonan-ujian-karya-akhir-bersyarat/',
      name: 'surat-permohonan-mengikuti-ujian-karya-akhir-bersyarat',
      component: PermohonanUjianBersyarat,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessSidang: true,
      },
    },
    {
      path: '/surat/pemesanan/',
      name: 'pemesanan-dokumen',
      component: DokumenAkademik,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/surat/tracking/',
      name: 'tracking-surat',
      component: TrackingPesanan,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/surat/tracking/:pk_key/detail/',
      name: 'detail-pengajuan-surat',
      component: DetailPengajuanSurat,
      props: true,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/',
      name: 'pengumuman',
      component: Pengumuman,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessPengumuman: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/create/',
      name: 'create-pengumuman',
      component: CreateAnnouncement,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessPengumuman: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/pengumuman/:pk_key/edit/',
      name: 'edit-pengumuman',
      component: EditAnnouncement,
      props: true,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessPengumuman: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/login/',
      name: 'login',
      component: Login,
      meta: {
        guest: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/register/',
      name: 'register',
      component: Register,
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/asisten/',
      name: 'asisten',
      component: AsdosPage,
      meta: {
        requiresAuth: true,
        requiresPrivilegeToAccessAsisten: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/admin/',
      name: 'admin',
      component: AdminPage,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
    {
      path: '/alumni/',
      name: 'alumni',
      component: AlumniPage,
      meta: {
        requiresAuth: true,
      },
      pathToRegexpOptions: {strict: true},
    },
  ],
});

router.beforeEach((to, from, next) => {
  const [url, param] = to.fullPath.split('?');
  const withoutTrailingSlash = RegExp('^.*[^/]$');

  if (withoutTrailingSlash.test(url)) {
    let nextUrl = url + '/';
    if (typeof(param) !== 'undefined') {
      nextUrl += '?' + param;
    }
    next(nextUrl);
    return;
  }

  const token = localStorage.token;
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (typeof(token) === 'undefined'
        || token === null || token === '') {
      next({name: 'login'});
      return;
    }
  }

  if (to.matched.some((record) => record.meta.guest)) {
    if (typeof(token) !== 'undefined'
        && token !== null && token !== '') {
      next({name: 'home'});
      return;
    }
  }

  const role = localStorage.getItem('role');
  const isAsdos = localStorage.getItem('is_asdos');
  const isAdmin = localStorage.getItem('is_admin');

  if (to.matched.some(
      (record) => record.meta.requiresPrivilegeToAccessPengumuman)) {
    if (role != 'mahasiswa' && role != 'staff'
        && isAsdos == 'false' && isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  if (to.matched.some(
      (record) => record.meta.requiresPrivilegeToAccessSidang)) {
    if (role != 'mahasiswa' && isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  if (to.name == 'create-pengumuman') {
    if (role != 'staff' && isAsdos == 'false' && isAdmin == 'false') {
      next({name: 'pengumuman'});
      return;
    }
  }

  if (to.name == 'asisten') {
    if (role != 'staff' && isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  if (to.name == 'admin') {
    if (isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  if (to.name == 'alumni') {
    if (isAdmin == 'false') {
      next({name: 'home'});
      return;
    }
  }

  next();
});

export default router;
