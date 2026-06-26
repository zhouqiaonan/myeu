from django.db.models import Q
from apps.users.models import UserDeptRole, Department

class ContextDataScopeMixin:
    """
    Context-aware Data Scope Parser Mixin.
    基于上下文的数据范围解析器。
    """
    data_scope_user_field = 'created_by'
    data_scope_dept_field = 'department_id' # 修改为直接关联数据的所属部门

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if not user or not user.is_authenticated:
            return queryset.none()

        if user.is_superuser:
            return queryset

        # 从请求头获取当前所在的部门上下文
        # Get current department context from request header
        dept_id = self.request.headers.get('X-Department-Id')
        if not dept_id:
            return queryset.none()

        # 获取用户在【当前部门】下的所有角色，并计算出最大的数据范围
        # Get all roles of the user in the CURRENT department and determine max scope
        user_dept_roles = UserDeptRole.objects.filter(user=user, department_id=dept_id).select_related('role')
        
        if not user_dept_roles.exists():
            return queryset.none()

        scopes = [udr.role.data_scope for udr in user_dept_roles]
        
        # Determine maximum scope / 确定最大范围
        if 'ALL' in scopes:
            data_scope = 'ALL'
        elif 'DEPARTMENT_AND_SUB' in scopes:
            data_scope = 'DEPARTMENT_AND_SUB'
        elif 'DEPARTMENT' in scopes:
            data_scope = 'DEPARTMENT'
        else:
            data_scope = 'SELF'

        # 根据计算出的范围进行过滤 / Filter queryset based on the determined scope
        if data_scope == 'ALL':
            return queryset
            
        elif data_scope == 'DEPARTMENT_AND_SUB':
            # 获取本部门及所有下级部门ID / Get current dept and all sub-depts IDs
            try:
                current_dept = Department.objects.get(id=dept_id)
                dept_ids = [current_dept.id]
                descendants = current_dept.get_all_descendants()
                dept_ids.extend([d.id for d in descendants])
                
                filter_kwargs = {f"{self.data_scope_dept_field}__in": dept_ids}
                return queryset.filter(**filter_kwargs)
            except Department.DoesNotExist:
                return queryset.none()
                
        elif data_scope == 'DEPARTMENT':
            # 仅本部门数据 / Only data of current department
            filter_kwargs = {self.data_scope_dept_field: dept_id}
            return queryset.filter(**filter_kwargs)
            
        else: # 'SELF'
            # 仅能看自己创建的数据 / Only self-created data
            filter_kwargs = {
                self.data_scope_user_field: user,
                self.data_scope_dept_field: dept_id  # 可选：确保即使是看自己的，也只能看当前部门下自己创建的
            }
            return queryset.filter(**filter_kwargs)
