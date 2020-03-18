import {shallowMount} from '@vue/test-utils';
import Login from '@/components/Login.vue';

describe('Tes login page', () => {
    const wrapper = shallowMount(Login);

    it ('apakah ada field username', () => {
        const field = wrapper.find({placeholder: 'username'});
        expect(field.exists()).toBe(true);
        expect(wrapper.html()).toContain('Username:');
    });

    it ('apakah ada field password', () => {
        const field = wrapper.find({placeholder: 'password'});
        expect(field.exists()).toBe(true);
        expect(wrapper.html()).toContain('Password:');
    })
})