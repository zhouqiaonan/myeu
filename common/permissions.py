from rest_framework.permissions import BasePermission
from users.models import UserDeptRole

class ContextRBACPermission(BasePermission):
    """
    Context-aware Role-Based Access Control Permission Class.
    基于上下文（当前部门）的角色权限校验类。
    """

    def has_permission(self, request, view):
        # 1. Check if user is authenticated / 验证用户是否已认证
        if not request.user or not request.user.is_authenticated:
            return False

        # 2. Superuser passes immediately / 如果是超级管理员，直接通过
        if request.user.is_superuser:
            return True

        # 3. Get current department context from request header / 从请求头获取当前所在的部门上下文
        # Frontend should pass this header when switching departments. / 前端切换部门时需在Header携带此参数
        dept_id = request.headers.get('X-Department-Id')
        if not dept_id:
            # If no department context is provided, deny access or fallback to default.
            # 如果未提供部门上下文，拒绝访问（或降级为默认部门）
            return False

        # 4. Get required permission code for the request / 获取当前请求所需的权限标识
        required_permission = self.get_required_permission(request, view)
        if not required_permission:
            return False

        # 5. Check if user has the permission in the SPECIFIC department / 检查用户在【当前部门】下的角色是否拥有该权限
        has_perm = UserDeptRole.objects.filter(
            user=request.user,
            department_id=dept_id,
            role__permissions__code=required_permission
        ).exists()

        return has_perm

    def get_required_permission(self, request, view):
        """
        Get required permission code for current API.
        获取当前接口需要的权限标识。
        """
        if hasattr(view, 'action') and hasattr(view, 'permission_code_map'):
            return view.permission_code_map.get(view.action)
        if hasattr(view, 'permission_code'):
            return view.permission_code
        return None
