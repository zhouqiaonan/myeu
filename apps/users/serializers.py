from rest_framework import serializers
from .models import User, Department, Role, UserDeptRole

class UserSerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    name = serializers.CharField(source='first_name', required=False)
    account = serializers.CharField(source='username', required=False)
    status = serializers.BooleanField(source='is_active', required=False)

    class Meta:
        model = User
        fields = ['id', 'account', 'name', 'email', 'phone', 'status', 'departments', 'roles', 'last_login']


    def get_departments(self, obj):
        # 英文: Extract department names from UserDeptRole relations
        # 中文: 从三元关联表中提取部门名称
        dept_roles = obj.dept_roles.select_related('department').all()
        depts = set([dr.department.name for dr in dept_roles if dr.department])
        return list(depts)

    def get_roles(self, obj):
        # 英文: Extract role names from UserDeptRole relations
        # 中文: 从三元关联表中提取角色名称
        dept_roles = obj.dept_roles.select_related('role').all()
        roles = set([dr.role.name for dr in dept_roles if dr.role])
        return list(roles)

