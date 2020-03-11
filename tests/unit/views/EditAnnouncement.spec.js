import {shallowMount} from '@vue/test-utils';
import EditAnnouncement from '@/views/EditAnnouncement';

describe('Tes Elemen Form', () => {
  const $route = {
    path: '/pengumuman/1/edit',
  };

  const wrapper = shallowMount(EditAnnouncement, {
    mocks: {
      $route,
    },
  });

  it('Edit Pengumuman page name : EditAnnouncement', () =>{
    expect(wrapper.name()).toEqual('EditAnnouncement');
  });
});
