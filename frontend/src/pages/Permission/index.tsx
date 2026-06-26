import React, { useState } from 'react';
import { Layout, Tabs, Tree, Input, Card } from 'antd';
import type { TreeDataNode } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import UserManagement from './UserManagement';
import RoleManagement from './RoleManagement';

const { Sider, Content } = Layout;

// 模拟部门树数据 / Mock department tree data
const initDeptTreeData: TreeDataNode[] = [
  {
    title: '总公司 (Headquarters)',
    key: '0',
    children: [
      { title: '财务部 (Finance)', key: '0-0' },
      { title: '采购部 (Purchasing)', key: '0-1' },
      { title: '销售部 (Sales)', key: '0-2' },
      { title: 'IT部 (IT)', key: '0-3' },
    ],
  },
  {
    title: '子公司 (Subsidiary)',
    key: '1',
    children: [
      { title: '行政部 (Administration)', key: '1-0' },
    ],
  },
];

const PermissionIndex: React.FC = () => {
  const [selectedDeptKeys, setSelectedDeptKeys] = useState<React.Key[]>(['0']);

  const onSelectDept = (selectedKeys: React.Key[]) => {
    setSelectedDeptKeys(selectedKeys);
  };

  return (
    <Layout style={{ background: '#fff', height: 'calc(100vh - 120px)' }}>
      {/* 左侧：部门树 (Left: Department Tree) */}
      <Sider width={250} style={{ background: '#fff', borderRight: '1px solid #f0f0f0', padding: '16px' }}>
        <div style={{ marginBottom: 16 }}>
          <Input placeholder="搜索部门 (Search Department)" prefix={<SearchOutlined />} />
        </div>
        <Tree
          defaultExpandAll
          selectedKeys={selectedDeptKeys}
          onSelect={onSelectDept}
          treeData={initDeptTreeData}
        />
      </Sider>

      {/* 右侧主区域 (Right Main Area) */}
      <Content style={{ padding: '0 24px', overflowY: 'auto' }}>
        <Tabs
          defaultActiveKey="1"
          items={[
            {
              key: '1',
              label: '用户管理 (User Mgmt)',
              children: <UserManagement selectedDept={selectedDeptKeys[0]} />,
            },
            {
              key: '2',
              label: '角色管理 (Role Mgmt)',
              children: <RoleManagement selectedDept={selectedDeptKeys[0]} />,
            },
            {
              key: '3',
              label: '部门管理 (Dept Mgmt)',
              children: <div>部门管理内容 (Department Management Content)</div>,
            },
          ]}
        />
      </Content>
    </Layout>
  );
};

export default PermissionIndex;
