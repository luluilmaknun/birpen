import {shallowMount} from '@vue/test-utils';
import AdminPage from '@/views/AdminPage';

import adminApi from '@/services/adminServices';

describe('Tes elements page', () => {
  let wrapper; let vm;

  beforeEach(() => {
    wrapper = shallowMount(AdminPage);

    adminApi.fetchAdmin = jest.fn(() => Promise.resolve({
      status: 200,
      data: {
        admin: [
          {
            pk: 0,
            username: 'lulu.aja',
          },
          {
            pk: 1,
            username: 'luulz',
          },
        ],
      },
    }));

    vm = wrapper.vm;
    vm.fetchAdmin();
  });

  it('update variable', () => {
    expect(vm.listAdmin.length).toBe(2);

    const usernames = wrapper.findAll('#username');
    expect(usernames.at(0).text())
        .toBe('lulu.aja');
    expect(usernames.at(1).text())
        .toBe('luulz');
  });
});
