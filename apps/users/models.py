from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    """
    Department Model
    部门模型
    """
    name = models.CharField(max_length=100, verbose_name=_("部门名称 (Department Name)"))
    code = models.CharField(max_length=50, unique=True, verbose_name=_("部门编码 (Department Code)"))
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name=_("上级部门 (Parent Department)"))
    is_active = models.BooleanField(default=True, verbose_name=_("状态 (Status)"))

    class Meta:
        db_table = "sys_department"

    def get_all_descendants(self):
        """
        Get all descendant departments recursively.
        递归获取所有下级部门。
        """
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_all_descendants())
        return descendants


class Permission(models.Model):
    """
    Permission Model (Menu, Button, API Data row logic)
    权限模型（菜单、按钮、API等）
    """
    PERM_TYPE_CHOICES = (
        ('MENU', _('菜单 (Menu)')),
        ('BUTTON', _('按钮 (Button)')),
        ('API', _('接口 (API)')),
    )
    name = models.CharField(max_length=100, verbose_name=_("权限名称 (Permission Name)"))
    code = models.CharField(max_length=100, unique=True, verbose_name=_("权限标识 (Permission Code)"))
    type = models.CharField(max_length=20, choices=PERM_TYPE_CHOICES, default='API', verbose_name=_("权限类型 (Type)"))
    
    class Meta:
        db_table = "sys_permission"


class Role(models.Model):
    """
    Role Model
    角色模型
    """
    DATA_SCOPE_CHOICES = (
        ('SELF', _('仅本人数据 (Self Data Only)')),
        ('DEPARTMENT', _('本部门数据 (Department Data)')),
        ('DEPARTMENT_AND_SUB', _('本部门及下级部门数据 (Department and Sub-department Data)')),
        ('ALL', _('全部数据 (All Data)')),
    )
    name = models.CharField(max_length=50, unique=True, verbose_name=_("角色名称 (Role Name)"))
    data_scope = models.CharField(max_length=20, choices=DATA_SCOPE_CHOICES, default='SELF', verbose_name=_("数据范围 (Data Scope)"))
    permissions = models.ManyToManyField(Permission, blank=True, related_name='roles', verbose_name=_("拥有权限 (Owned Permissions)"))

    class Meta:
        db_table = "sys_role"


class User(AbstractUser):
    """
    Custom User Model
    自定义用户模型
    注意：移除了直接的 department 和 roles 外键，改为通过 UserDeptRole 中间表关联。
    Note: Removed direct department and roles foreign keys, use UserDeptRole instead.
    """
    class Meta:
        db_table = "sys_user"


class UserDeptRole(models.Model):
    """
    User-Department-Role Associative Entity (Ternary Relationship)
    用户-部门-角色 关联表（三元关系：解决同一用户在不同部门拥有不同角色的需求）
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dept_roles')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_depts')

    class Meta:
        db_table = "sys_user_dept_role"
        unique_together = ('user', 'department', 'role')
        verbose_name = _("用户部门角色关联 (User Dept Role)")
