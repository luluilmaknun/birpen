import axios from 'axios';
import Cookies from 'js-cookie';

const token = localStorage.getItem('token');

export default axios.create({
  baseURL: '/api',
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
    'X-CSRFToken': Cookies.get('csrftoken'),
  },
});
