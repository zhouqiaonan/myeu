import axios from 'axios';
import { message } from 'antd';

// 创建 axios 实例 / Create axios instance
const request = axios.create({
  baseURL: '/', // 配合 Vite proxy / Works with Vite proxy
  timeout: 10000,
});

// 请求拦截器 / Request interceptor
request.interceptors.request.use(
  (config) => {
    // 从 localStorage 获取 token / Get token from localStorage
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器 / Response interceptor
request.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    const { response } = error;
    if (response) {
      // 统一错误处理 / Global error handling
      switch (response.status) {
        case 401:
          message.error('未授权，请重新登录 / Unauthorized, please login again');
          // 可在这里处理登出逻辑，如清空 token，跳转到登录页 / Handle logout logic here
          localStorage.removeItem('access_token');
          window.location.href = '/login';
          break;
        case 403:
          message.error('拒绝访问 / Access denied');
          break;
        case 404:
          message.error('请求错误，未找到该资源 / Resource not found');
          break;
        case 500:
          message.error('服务器端出错 / Internal server error');
          break;
        default:
          message.error(response.data?.detail || '网络错误 / Network error');
      }
    } else {
      message.error('服务器连接失败 / Server connection failed');
    }
    return Promise.reject(error);
  }
);

export default request;
