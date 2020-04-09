import axios from 'axios';
import Cookies from 'js-cookie';

const token = sessionStorage.token;

export default axios.create({
  baseURL: '/api',
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
<<<<<<< HEAD
    'Authorization': `Token ${token}`,
=======
    'Authorization': `Bearer ${token}`,
>>>>>>> c6465f5f2f779f0fb0a29e2be10f00e69353045f
    'X-CSRFToken': Cookies.get('csrftoken'),
  },
});
