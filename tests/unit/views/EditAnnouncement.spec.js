import {shallowMount} from '@vue/test-utils';
import EditAnnouncement from '@/views/EditAnnouncement';

describe('Tes Elemen Form', () => {
  const wrapper = shallowMount(EditAnnouncement);

  it('Edit Pengumuman page name : EditAnnouncement', () =>{
    expect(wrapper.name()).toEqual('EditAnnouncement');
  });
});
