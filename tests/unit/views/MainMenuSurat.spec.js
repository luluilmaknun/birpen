import {shallowMount} from '@vue/test-utils';
import MainMenuSurat from '@/views/MainMenuSurat.vue';

const pageRouteList = ['sidang', 'pemesanan', 'tracking'];

const baseRoute = 'surat';

const $route = {
  path: baseRoute,
};

const $router = {
  push(dictPath) {
    $route.path = baseRoute + '/' + dictPath.path;
  },
};

describe('Tes Elemen Halaman Main Menu Surat', () => {
  const wrapper = shallowMount(MainMenuSurat);

  it('Main Menu Surat name : MainMenuSurat', () =>{
    expect(wrapper.name()).toEqual('MainMenuSurat');
  });

  it('terdapat button Dokumen Sidang Akhir', () => {
    const buttonPengumuman = wrapper
        .find('#button_dokumen_sidang_akhir');

    expect(buttonPengumuman.exists()).toBe(true);
    expect(buttonPengumuman.html())
        .toContain('Dokumen Kelengkapan Sidang Karya Akhir');
  });

  it('terdapat button Pemesanan Dokumen Akademik', () => {
    const buttonSurat = wrapper
        .find('#button_pemesanan_dokumen');

    expect(buttonSurat.exists()).toBe(true);
    expect(buttonSurat.html())
        .toContain('Pemesanan Dokumen Akademik');
  });

  it('terdapat button Trace & Tracking Pemesanan', () => {
    const buttonSurat = wrapper
        .find('#button_tracking_pemesanan');

    expect(buttonSurat.exists()).toBe(true);
    expect(buttonSurat.html().replace(/&amp;/g, '&'))
        .toContain('Trace & Tracking Pemesanan Dokumen Akademik');
  });
});

describe('Tes fungsionalitas fungsi', () => {
  const wrapper = shallowMount(MainMenuSurat, {
    mocks: {
      $router,
      $route,
    },
  });
  const vm = wrapper.vm;

  it('goToPage() method', () => {
    for (let i = 1; i < pageRouteList.length; i++) {
      vm.goToPage(pageRouteList[i]);
      const pageRouteName = vm.$route.path.split('/').slice(-1)[0];
      expect(pageRouteName).toEqual(pageRouteList[i]);
    }
  });
});
