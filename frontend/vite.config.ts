import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // 代理 API 请求到 Django 服务器
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      // 代理 admin 页面到 Django 服务器
      '/admin': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      }
    }
  }
})
