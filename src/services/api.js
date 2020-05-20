import axios from 'axios';
import Cookies from 'js-cookie';

const token = localStorage.token;

const instance = axios.create({
  baseURL: '/api',
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
    'X-CSRFToken': Cookies.get('csrftoken'),
  },
});

instance.interceptors.response.use((response) => {
  const ApiURL = response.config.url;
  const id = ApiURL.split('/').filter(Boolean).slice(1).join('_');

  while (document.getElementById('loader_'+id)) {
    document.getElementById('loader_'+id).remove();
  }

  let content;
  while (document.getElementById(id)) {
    content = document.getElementById(id);
    content.replaceWith(...content.childNodes);
  }

  return response;
});

export default instance;
