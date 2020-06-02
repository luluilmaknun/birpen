import {shallowMount} from '@vue/test-utils';
import BackBtn from '@/components/btn-kembali';

describe('tombol kembali', () => {
  const wrapper = shallowMount(BackBtn);

  it('tes klik tombol kembali', () => {
    expect(wrapper.find('#back-btn').exists()).toBe(true);
    const button = wrapper.find('#back-btn');
    button.trigger('click');
  });
});
