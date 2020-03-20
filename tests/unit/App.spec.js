import {shallowMount} from '@vue/test-utils';
import Navigation from '@/App.vue';

describe('Tes Halaman Utama', () => {
  const wrapper = shallowMount(Navigation);

  it('App name : Navigation', () =>{
    expect(wrapper.name()).toEqual(undefined);
  });
});
