import {mount} from '@vue/test-utils';
import DatePicker from '@/components/date-picker.vue';

describe('DatePicker', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(DatePicker);
    expect(wrapper.isVueInstance()).toBeTruthy();
  });
});
