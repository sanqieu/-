import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
  timeout: 5000
})

// 请求拦截器，可自动加token
instance.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default instance