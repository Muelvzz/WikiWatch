import axios from 'axios';

const isProduction = import.meta.env.PROD;
const RENDER_URL = import.meta.env.VITE_API_URL; 
const LOCAL_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: isProduction ? RENDER_URL : LOCAL_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;