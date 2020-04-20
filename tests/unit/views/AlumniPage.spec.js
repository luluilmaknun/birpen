import {shallowMount} from '@vue/test-utils';
import AlumniPage from '@/views/AlumniPage';
import alumniApi from '@/services/alumniServices';

describe('tes fetch alumni di alumni page', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(AlumniPage);
    alumniApi.fetchAlumni = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        alumni: [
          {
            pk: 0,
            username: 'muhammad.yusuf',
            email: 'muhammad_yusuf@gmail.com',
            is_blacklist: true,
          },
          {
            pk: 1,
            username: 'aisyah',
            email: 'aisyah_soleh@gmail.com',
            is_blacklist: false,
          },

        ],
      },
    }));

    vm = wrapper.vm;
    vm.fetchAlumni();
  });

  it('tes fetch alumni sukses', () => {
    expect(vm.listAlumni.length).toBe(2);
  });
});
