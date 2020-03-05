import {shallowMount} from '@vue/test-utils';
import Home from '@/Home.vue';

const pageRouteList = ['pengumuman', 'surat'];

const baseRoute = '';

const $route = {
  path: baseRoute,
};

const $router = {
  push(dictPath) {
    $route.path = baseRoute + '/' + dictPath.path;
  },
};

describe('Tes Halaman Utama', () => {
  const wrapper = shallowMount(Home, {
    mocks: {
      $route,
      $router,
    },
  });
  const vm = wrapper.vm;

  it('Halaman Utama name : Home', () =>{
    expect(wrapper.name()).toEqual('Home');
  });

  it('apakah halaman utama mengandung button Pengumuman', () => {
    const buttonPengumuman = wrapper.find('#button_pengumuman');
    expect(buttonPengumuman.exists()).toBe(true);
    expect(buttonPengumuman.html()).toContain('Pengumuman Perkuliahan');
  });

  it('apakah halaman utama mengandung button Surat', () => {
    const buttonSurat = wrapper.find('#button_surat');
    expect(buttonSurat.exists()).toBe(true);
    expect(buttonSurat.html()).toContain('Layanan Dokumen Akademik');
  });

  it('goToPage() method', () => {
    for (let i = 1; i < pageRouteList.length; i++) {
      vm.goToPage(pageRouteList[i]);
      const pageRouteName = vm.$route.path.split('/').slice(-1)[0];
      expect(pageRouteName).toEqual(pageRouteList[i]);
    }
  });
});
