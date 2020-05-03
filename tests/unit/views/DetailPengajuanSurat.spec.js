import {shallowMount} from '@vue/test-utils';
import DetailPengajuanSurat from '@/views/DetailPengajuanSurat.vue';

describe('Cek komponen profile', () => {
  let wrapper;
  wrapper = shallowMount(DetailPengajuanSurat);
  it('Cek profile Component', () => {
    const div = wrapper.find('.profile-detail');
    expect(div.exists()).toBe(true);
  });

  it('Cek profile detail', () => {
    wrapper = shallowMount(DetailPengajuanSurat, {
      data() {
        return {
          'profileDetail': {
            'nama': 'sebuah nama',
            'npm': '1706075022',
            'id_pesanan': '170DFC',
          },
        };
      },
    });
    expect(wrapper.find('#profile-nama').html()).toContain('sebuah nama');
    expect(wrapper.find('#profile-npm').html()).toContain('1706075022');
    expect(wrapper.find('#profile-idPesanan').html()).toContain('170DFC');
  });
});
