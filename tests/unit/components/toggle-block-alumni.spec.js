import {shallowMount} from '@vue/test-utils';
import ToggleBlockAlumni from '@/components/toggle-block-alumni.vue';
import alumniServices from '@/services/alumniServices';

describe('tes component', () => {
  const wrapper = shallowMount(ToggleBlockAlumni);

  it('tes klik tombol trigger fungsi open modal', () => {
    expect(wrapper.find('#unblock-btn').exists()).toBe(true);
    const blokirButton = wrapper.find('#unblock-btn');
    blokirButton.trigger('click');
  });

  it('tes klik tombol trigger fungsi close modal', () => {
    expect(wrapper.find('#tidak-btn').exists()).toBe(true);
    const blokirButton = wrapper.find('#tidak-btn');
    blokirButton.trigger('click');
  });
});

describe('tes toggle blokir', () => {
  let wrapper; let vm;

  it('sukses blok', () => {
    wrapper = shallowMount(ToggleBlockAlumni, {
      data() {
        return {
          'alumni_username': 'muhammad.reza',
          'is_blocked': false,
          'error_message': '',
        };
      },
    });

    alumniServices.toggleBlockAlumni = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        success: 'True',
      },
    }));

    vm = wrapper.vm;
    vm.toggle_alumni();
  });

  it('gagal blok', () => {
    wrapper = shallowMount(ToggleBlockAlumni, {
      data() {
        return {
          'alumni_username': 'muhammad.reza',
          'is_blocked': false,
          'error_message': 'Alumni tidak ada.',
        };
      },
    });

    alumniServices.toggleBlockAlumni = jest.fn(() => Promise.resolve({
      status: 400,
      data: {
        detail: 'Alumni tidak ada.',
      },
    }));

    vm = wrapper.vm;
    vm.toggle_alumni();
    expect(vm.error_message).toEqual('Alumni tidak ada.');
  });
});
