import React, { useState } from 'react';
import { Table, Button, Space, Modal, Tree, Form, Input, Select, Radio } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SettingOutlined } from '@ant-design/icons';
import type { TreeDataNode } from 'antd';

const { Option } = Select;

interface RoleManagementProps {
  selectedDept: React.Key;
}

// 模拟权限树数据 / Mock permission tree data
const permissionTreeData: TreeDataNode[] = [
  {
    title: '采购管理 (Purchasing)',
    key: 'pur',
    children: [
      {
        title: '采购订单 (Orders)',
        key: 'pur-order',
        children: [
          { title: '查看 (View)', key: 'pur-order-view' },
          { title: '新增 (Create)', key: 'pur-order-create' },
          { title: '编辑 (Edit)', key: 'pur-order-edit' },
          { title: '删除 (Delete)', key: 'pur-order-delete' },
          { title: '审核 (Audit)', key: 'pur-order-audit' },
        ],
      },
      { title: '采购退货 (Returns)', key: 'pur-return' },
    ],
  },
  {
    title: '财务管理 (Finance)',
    key: 'fin',
    children: [
      { title: '凭证管理 (Vouchers)', key: 'fin-voucher' },
      { title: '报表查看 (Reports)', key: 'fin-report' },
    ],
  },
  {
    title: '库存管理 (Inventory)',
    key: 'inv',
    children: [
      { title: '入库单 (Inbound)', key: 'inv-in' },
      { title: '出库单 (Outbound)', key: 'inv-out' },
    ],
  },
];

const RoleManagement: React.FC<RoleManagementProps> = ({ selectedDept }) => {
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  const [checkedKeys, setCheckedKeys] = useState<React.Key[]>(['pur-order-view', 'pur-order-edit', 'pur-order-audit', 'fin-voucher', 'fin-report']);

  const columns = [
    { title: '角色名称 (Role Name)', dataIndex: 'name', key: 'name' },
    { title: '所属部门 (Department)', dataIndex: 'dept', key: 'dept' },
    { title: '数据权限 (Data Scope)', dataIndex: 'dataScope', key: 'dataScope' },
    {
      title: '操作 (Actions)',
      key: 'action',
      render: () => (
        <Space size="middle">
          <Button type="link" icon={<EditOutlined />}>编辑 (Edit)</Button>
          <Button type="link" icon={<SettingOutlined />} onClick={() => setIsAuthModalOpen(true)}>分配权限 (Assign Perms)</Button>
          <Button type="link" danger icon={<DeleteOutlined />}>删除 (Delete)</Button>
        </Space>
      ),
    },
  ];

  const data = [
    { key: '1', name: '会计 (Accountant)', dept: '财务部', dataScope: '本部门数据 (Dept Only)' },
    { key: '2', name: '出纳 (Cashier)', dept: '财务部', dataScope: '仅本人数据 (Self Only)' },
  ];

  const onCheck = (checkedKeysValue: any) => {
    setCheckedKeys(checkedKeysValue as React.Key[]);
  };

  return (
    <div>
      <Space style={{ marginBottom: 16 }}>
        <Button type="primary" icon={<PlusOutlined />}>新增角色 (Add Role)</Button>
      </Space>
      
      <Table columns={columns} dataSource={data} />

      {/* 权限分配弹窗 / Permission Assignment Modal */}
      <Modal
        title="🔐 分配权限 - 会计 (Assign Permissions - Accountant)"
        open={isAuthModalOpen}
        onCancel={() => setIsAuthModalOpen(false)}
        width={600}
      >
        <Form layout="vertical">
          <Form.Item label="角色名称 (Role Name)">
            <Input value="会计 (Accountant)" disabled />
          </Form.Item>
          
          <Form.Item label="数据权限范围控制 (Data Scope Control)">
            <Radio.Group defaultValue="dept">
              <Space direction="vertical">
                <Radio value="self">仅本人数据 (Self Only)</Radio>
                <Radio value="dept">本部门数据 (Department Data)</Radio>
                <Radio value="dept_sub">本部门及子部门数据 (Dept & Sub-depts)</Radio>
                <Radio value="all">全部数据 (All Data)</Radio>
              </Space>
            </Radio.Group>
          </Form.Item>

          <Form.Item label="功能权限分配 (Function Permissions)">
            <div style={{ border: '1px solid #d9d9d9', borderRadius: '4px', padding: '10px', maxHeight: '300px', overflowY: 'auto' }}>
              <Tree
                checkable
                defaultExpandAll
                checkedKeys={checkedKeys}
                onCheck={onCheck}
                treeData={permissionTreeData}
              />
            </div>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default RoleManagement;
