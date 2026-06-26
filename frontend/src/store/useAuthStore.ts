import { create } from 'zustand';

interface AuthState {
  token: string | null;
  setToken: (token: string) => void;
  logout: () => void;
}

// 使用 Zustand 管理认证状态 / Use Zustand to manage authentication state
const useAuthStore = create<AuthState>((set) => ({
  token: localStorage.getItem('access_token'),
  setToken: (token: string) => {
    localStorage.setItem('access_token', token);
    set({ token });
  },
  logout: () => {
    localStorage.removeItem('access_token');
    set({ token: null });
  },
}));

export default useAuthStore;
