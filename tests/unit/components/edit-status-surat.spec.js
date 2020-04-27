import {shallowMount} from '@vue/test-utils';
import EditStatusSurat from '@/components/edit-status-surat.vue';

describe('tes elemen edit status surat component', () => {
  const wrapper = shallowMount(EditStatusSurat);

  it('tes edit button', () => {
    expect(wrapper.find('#id-edit-status-button').exists()).toBe(true);
    const button = wrapper.find('#id-edit-status-button');
    button.trigger('click');
  });

  it('tes simpan button', () => {
    expect(wrapper.find('#id-simpan-button').exists()).toBe(true);
    const button = wrapper.find('#id-simpan-button');
    button.trigger('click');
  });
});
