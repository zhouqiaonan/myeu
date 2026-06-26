import React, { useState, useEffect } from 'react';
import { Modal, Form, Input, Switch, Button, Select, Space, Divider, Typography, message } from 'antd';
import { PlusOutlined, DeleteOutlined } from '@ant-design/icons';
import request from '../../utils/request';

const { Option } = Select;
const { Title, Text } = Typography;

interface UserEditModalProps {
  open: boolean;
  onCancel: () => void;
  userData: any | null;
}

// 模拟的部门与角色字典数据 / Mock dictionary data for depts and roles
const deptOptions = [
  { label: '财务部 (Finance)', value: 'dept_1' },
  { label: '采购部 (Purchasing)', value: 'dept_2' },
  { label: 'IT部 (IT)', value: 'dept_3' },
];

const roleOptionsMap: Record<string, { label: string, value: string }[]> = {
  'dept_1': [{ label: '会计 (Accountant)', value: 'role_1' }, { label: '审核 (Auditor)', value: 'role_2' }],
  'dept_2': [{ label: '经理 (Manager)', value: 'role_3' }, { label: '专员 (Specialist)', value: 'role_4' }],
  'dept_3': [{ label: '管理员 (Admin)', value: 'role_5' }],
};

const UserEditModal: React.FC<UserEditModalProps> = ({ open, onCancel, userData }) => {
  const [form] = Form.useForm();
  
  // 核心：维护一个数组来记录多行“部门-角色” / Core: Maintain an array for multi-row "Dept-Role"
  const [deptRoles, setDeptRoles] = useState<{ id: number, dept: string | null, role: string | null }[]>([
    { id: Date.now(), dept: null, role: null }
  ]);

  useEffect(() => {
    if (open) {
      if (userData) {
        form.setFieldsValue({
          name: userData.name,
          account: userData.account,
          phone: userData.phone,
          email: userData.email,
          status: userData.status,
        });
        // 模拟数据回显 (Mock data echo)
        setDeptRoles([{ id: Date.now(), dept: 'dept_1', role: 'role_1' }]);
      } else {
        form.resetFields();
        setDeptRoles([{ id: Date.now(), dept: null, role: null }]);
      }
    }
  }, [open, userData, form]);

  const handleAddDeptRole = () => {
    setDeptRoles([...deptRoles, { id: Date.now(), dept: null, role: null }]);
  };

  const handleRemoveDeptRole = (id: number) => {
    if (deptRoles.length === 1) return; // 至少保留一条 (Keep at least one)
    setDeptRoles(deptRoles.filter(item => item.id !== id));
  };

  const handleDeptChange = (id: number, value: string) => {
    setDeptRoles(deptRoles.map(item => {
      if (item.id === id) {
        return { ...item, dept: value, role: null }; // 切换部门时清空已选角色 (Clear role when dept changes)
      }
      return item;
    }));
  };

  const handleRoleChange = (id: number, value: string) => {
    setDeptRoles(deptRoles.map(item => {
      if (item.id === id) {
        return { ...item, role: value };
      }
      return item;
    }));
  };

  const handleSave = () => {
    form.validateFields().then(async (values) => {
      console.log('Form Values:', values);
      console.log('Dept Roles:', deptRoles);
      
      try {
        const payload = {
          ...values,
          deptRoles: deptRoles,
        };

        if (userData) {
          // 编辑用户 (Edit user)
          await request.put(`/api/users/users/${userData.key}/`, payload);
          message.success('用户更新成功 (User updated successfully)');
        } else {
          // 新增用户 (Add user)
          await request.post('/api/users/users/', payload);
          message.success('用户创建成功 (User created successfully)');
        }
        onCancel();
      } catch (error) {
        console.error('Failed to save user:', error);
        // Error message is already handled by axios interceptor
      }
    });
  };

  return (
    <Modal
      title={userData ? `编辑用户 - ${userData.name} (Edit User)` : '新增用户 (Add User)'}
      open={open}
      onCancel={onCancel}
      onOk={handleSave}
      width={700}
      destroyOnClose
    >
      <Form form={form} layout="vertical" initialValues={{ status: true }}>
        <Title level={5}>基本信息 (Basic Info)</Title>
        <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
          <Form.Item name="name" label="用户名 (Name)" rules={[{ required: true }]} style={{ width: 300 }}>
            <Input />
          </Form.Item>
          <Form.Item name="account" label="登录账号 (Account)" rules={[{ required: true }]} style={{ width: 300 }}>
            <Input />
          </Form.Item>
        </Space>
        
        <Space style={{ display: 'flex', marginBottom: 8 }} align="baseline">
          <Form.Item name="phone" label="手机号 (Phone)" style={{ width: 300 }}>
            <Input />
          </Form.Item>
          <Form.Item name="email" label="邮箱 (Email)" style={{ width: 300 }}>
            <Input />
          </Form.Item>
        </Space>

        <Form.Item name="status" label="状态 (Status)" valuePropName="checked">
          <Switch checkedChildren="启用 (Active)" unCheckedChildren="禁用 (Disabled)" />
        </Form.Item>

        <Divider />

        <Title level={5}>部门与角色核心配置 (Dept & Role Configuration)</Title>
        <Text type="secondary" style={{ display: 'block', marginBottom: 16 }}>
          * 说明：一个用户可属于多个部门，每个部门下可拥有不同角色。(A user can belong to multiple depts with different roles)
        </Text>

        {/* 动态增删部门角色行 / Dynamic Dept-Role Rows */}
        {deptRoles.map((item, index) => (
          <Space key={item.id} style={{ display: 'flex', marginBottom: 8 }} align="baseline">
            <Form.Item label={index === 0 ? "部门 (Department)" : ""} required>
              <Select 
                style={{ width: 200 }} 
                placeholder="选择部门 (Select Dept)" 
                value={item.dept}
                onChange={(val) => handleDeptChange(item.id, val)}
              >
                {deptOptions.map(opt => <Option key={opt.value} value={opt.value}>{opt.label}</Option>)}
              </Select>
            </Form.Item>

            <Form.Item label={index === 0 ? "角色 (Role)" : ""} required>
              <Select 
                style={{ width: 200 }} 
                placeholder="选择角色 (Select Role)" 
                value={item.role}
                onChange={(val) => handleRoleChange(item.id, val)}
                disabled={!item.dept}
              >
                {item.dept && roleOptionsMap[item.dept] ? (
                  roleOptionsMap[item.dept].map(opt => <Option key={opt.value} value={opt.value}>{opt.label}</Option>)
                ) : null}
              </Select>
            </Form.Item>

            <Form.Item label={index === 0 ? "操作 (Action)" : ""}>
              <Button 
                danger 
                icon={<DeleteOutlined />} 
                onClick={() => handleRemoveDeptRole(item.id)}
                disabled={deptRoles.length === 1}
              >
                删除 (Delete)
              </Button>
            </Form.Item>
          </Space>
        ))}

        <Button type="dashed" onClick={handleAddDeptRole} icon={<PlusOutlined />} style={{ width: '100%', marginTop: 8 }}>
          添加部门角色 (Add Dept-Role)
        </Button>

      </Form>
    </Modal>
  );
};

export default UserEditModal;
