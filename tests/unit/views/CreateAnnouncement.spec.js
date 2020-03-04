import {shallowMount} from '@vue/test-utils';
import CreateAnnouncement from '@/views/CreateAnnouncement';

describe('Tes Buat Pengumuman page', () => {
  const props = {

  };

  const wrapper = shallowMount(CreateAnnouncement, {
    props,
  });

  it('Buat Pengumuman page name : CreateAnnouncement', () =>{
    expect(wrapper.name()).toEqual('CreateAnnouncement');
  });

  it('punya elemen nama pembuat', () => {
    expect(wrapper.contains('p#pembuat')).toBe(true);
  });

  it('punya elemen nama mata kuliah', () => {
    expect(wrapper.contains('select#nama_mata_kuliah')).toBe(true);
  });

  it('punya elemen jenis pengumuman', () => {
    expect(wrapper.contains('select#jenis_pengumuman')).toBe(true);
  });

  it('punya elemen nama dosen', () => {
    expect(wrapper.contains('input#nama_dosen')).toBe(true);
  });

  it('punya elemen nama ruang', () => {
    expect(wrapper.contains('select#nama_ruang')).toBe(true);
  });

  it('punya elemen nama sesi', () => {
    expect(wrapper.contains('select#nama_sesi')).toBe(true);
  });

  it('punya elemen nama status pengumuman', () => {
    expect(wrapper.contains('select#nama_status_pengumuman')).toBe(true);
  });

  it('punya elemen komen', () => {
    expect(wrapper.contains('textarea#komentar')).toBe(true);
  });

  it('Tes submit form', () =>{
    wrapper.find('[type=\'submit\']').trigger('click');
  });
});
