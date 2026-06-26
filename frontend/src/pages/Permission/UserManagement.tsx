import React, { useState } from 'react';
import { Table, Button, Input, Select, Space, Tag, Switch, Modal } from 'antd';
import { SearchOutlined, PlusOutlined, EditOutlined, DeleteOutlined, ExclamationCircleOutlined } from '@ant-design/icons';
import UserEditModal from './UserEditModal';

const { Option } = Select;
const { confirm } = Modal;

interface UserManagementProps {
  selectedDept: React.Key;
}

// 模拟数据类型 / Mock data type
interface DataType {
  key: string;
  name: string;
  account: string;
  departments: string[];
  roles: string[];
  status: boolean;
  lastLogin: string;
}

const mockData: DataType[] = [
  {
    key: '1',
    name: '张三 (Zhang San)',
    account: 'zhangs',
    departments: ['财务部'],
    roles: ['会计'],
    status: true,
    lastLogin: '2023-10-25 10:20:00',
  },
  {
    key: '2',
    name: '李四 (Li Si)',
    account: 'lisi',
    departments: ['采购部', '行政部'],
    roles: ['经理', '专员'],
    status: true,
    lastLogin: '2023-10-26 09:15:00',
  },
  {
    key: '3',
    name: '王五 (Wang Wu)',
    account: 'wangwu',
    departments: ['财务部'],
    roles: ['审核'],
    status: false,
    lastLogin: '2023-10-20 14:30:00',
  },
];

const UserManagement: React.FC<UserManagementProps> = ({ selectedDept }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingUser, setEditingUser] = useState<DataType | null>(null);

  const handleAdd = () => {
    setEditingUser(null);
    setIsModalOpen(true);
  };

  const handleEdit = (record: DataType) => {
    setEditingUser(record);
    setIsModalOpen(true);
  };

  const handleDelete = (record: DataType) => {
    confirm({
      title: '确认删除 (Confirm Delete)',
      icon: <ExclamationCircleOutlined />,
      content: `确定要删除用户 ${record.name} 吗？(Are you sure you want to delete ${record.name}?)`,
      onOk() {
        console.log('Deleted:', record.key);
      },
    });
  };

  const columns = [
    {
      title: '姓名 (Name)',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: '账号 (Account)',
      dataIndex: 'account',
      key: 'account',
    },
    {
      title: '部门 (Departments)',
      dataIndex: 'departments',
      key: 'departments',
      render: (departments: string[]) => (
        <>
          {departments.map((dept) => (
            <Tag color="blue" key={dept}>
              {dept}
            </Tag>
          ))}
        </>
      ),
    },
    {
      title: '角色 (Roles)',
      dataIndex: 'roles',
      key: 'roles',
      render: (roles: string[]) => roles.join(', '),
    },
    {
      title: '状态 (Status)',
      dataIndex: 'status',
      key: 'status',
      render: (status: boolean) => (
        <Switch checkedChildren="启用" unCheckedChildren="禁用" defaultChecked={status} />
      ),
    },
    {
      title: '操作 (Actions)',
      key: 'action',
      render: (_: any, record: DataType) => (
        <Space size="middle">
          <Button type="link" icon={<EditOutlined />} onClick={() => handleEdit(record)}>
            编辑 (Edit)
          </Button>
          <Button type="link" danger icon={<DeleteOutlined />} onClick={() => handleDelete(record)}>
            删除 (Delete)
          </Button>
        </Space>
      ),
    },
  ];

  return (
    <div>
      {/* 搜索与操作区域 (Search and Action Area) */}
      <Space style={{ marginBottom: 16, display: 'flex', justifyContent: 'space-between', width: '100%' }}>
        <Space>
          <Input placeholder="姓名/账号 (Name/Account)" style={{ width: 200 }} />
          <Select placeholder="角色 (Role)" style={{ width: 120 }} allowClear>
            <Option value="会计">会计 (Accountant)</Option>
            <Option value="经理">经理 (Manager)</Option>
          </Select>
          <Select placeholder="状态 (Status)" style={{ width: 100 }} allowClear>
            <Option value="true">启用 (Active)</Option>
            <Option value="false">禁用 (Disabled)</Option>
          </Select>
          <Button type="primary" icon={<SearchOutlined />}>搜索 (Search)</Button>
          <Button>重置 (Reset)</Button>
        </Space>
        <Space>
          <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>新增用户 (Add User)</Button>
          <Button danger>批量删除 (Batch Delete)</Button>
        </Space>
      </Space>

      {/* 列表区域 (List Area) */}
      <Table 
        rowSelection={{ type: 'checkbox' }} 
        columns={columns} 
        dataSource={mockData} 
        pagination={{ total: 42, showSizeChanger: true, showQuickJumper: true }}
      />

      {/* 新增/编辑弹窗 (Add/Edit Modal) */}
      <UserEditModal 
        open={isModalOpen} 
        onCancel={() => setIsModalOpen(false)} 
        userData={editingUser} 
      />
    </div>
  );
};

export default UserManagement;
