import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Layout, Menu, Typography, Button } from 'antd';
import useAuthStore from './store/useAuthStore';
import PermissionIndex from './pages/Permission';

const { Header, Content, Footer } = Layout;
const { Title } = Typography;

// 首页组件 / Home Component
const Home = () => (
  <div style={{ textAlign: 'center', marginTop: '50px' }}>
    <Title level={2}>欢迎来到现代化 Django + React 项目</Title>
    <p>这是一个使用 Vite, React 18, TypeScript, Ant Design 和 Zustand 构建的前端应用。</p>
  </div>
);

// 仪表盘组件 / Dashboard Component
const Dashboard = () => {
  const { token, logout } = useAuthStore();
  
  return (
    <div style={{ padding: '20px' }}>
      <Title level={3}>仪表盘 (Dashboard)</Title>
      {token ? (
        <div>
          <p>已登录，您的 Token 是：{token}</p>
          <Button type="primary" danger onClick={logout}>退出登录 (Logout)</Button>
        </div>
      ) : (
        <p>您尚未登录，请先登录以查看更多信息。</p>
      )}
    </div>
  );
};

// 根组件 / Root App Component
function App() {
  const { token, setToken } = useAuthStore();

  const handleSimulateLogin = () => {
    setToken('simulated_jwt_token_123456');
  };

  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        <Header style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div className="logo" style={{ color: 'white', fontSize: '20px', fontWeight: 'bold' }}>
            My App
          </div>
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['1']}
            items={[
              { key: '1', label: <Link to="/">首页 (Home)</Link> },
              { key: '2', label: <Link to="/dashboard">仪表盘 (Dashboard)</Link> },
              { key: '3', label: <Link to="/permission">权限管理 (Permission)</Link> },
            ]}
            style={{ flex: 1, minWidth: 0, marginLeft: '20px' }}
          />
          {!token && (
            <Button type="primary" onClick={handleSimulateLogin}>
              模拟登录 (Simulate Login)
            </Button>
          )}
        </Header>
        <Content style={{ padding: '0 48px' }}>
          <div
            style={{
              background: '#fff',
              minHeight: 280,
              padding: 24,
              marginTop: 24,
              borderRadius: 8,
            }}
          >
            {/* 定义路由规则 / Define Routing Rules */}
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/permission" element={<PermissionIndex />} />
            </Routes>
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          My App ©{new Date().getFullYear()} Created with Ant Design
        </Footer>
      </Layout>
    </Router>
  );
}

export default App;
