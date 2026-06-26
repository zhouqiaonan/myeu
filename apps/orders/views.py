from rest_framework import viewsets
from rest_framework.response import Response
from common.permissions import RBACPermission
from common.mixins import DataScopeMixin

# 假设存在以下模型和序列化器 (Assuming the following model and serializer exist)
# from orders.models import Order
# from orders.serializers import OrderSerializer

class OrderViewSet(DataScopeMixin, viewsets.ModelViewSet):
    """
    订单视图集示例 (Example Order ViewSet)
    演示如何结合 RBACPermission 和 DataScopeMixin 进行权限与数据范围控制。
    (Demonstrates how to combine RBACPermission and DataScopeMixin for auth and data scope control)
    """
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    
    # 1. 应用自定义的 RBAC 权限校验类 (Apply custom RBAC permission class)
    permission_classes = [RBACPermission]
    
    # 2. 映射不同 action 对应的权限标识 (Map actions to permission codes)
    # 格式：app_label.action_model
    permission_code_map = {
        'list': 'orders.view_order',
        'retrieve': 'orders.view_order',
        'create': 'orders.create_order',
        'update': 'orders.update_order',
        'partial_update': 'orders.update_order',
        'destroy': 'orders.delete_order',
    }

    # 3. 告诉 DataScopeMixin，模型中哪个字段代表用户，哪个字段代表部门
    # (Tell DataScopeMixin which fields represent user and department in the model)
    data_scope_user_field = 'created_by'  # 假设 Order 模型中有 created_by 外键指向 User
    data_scope_dept_field = 'created_by__department'

    def list(self, request, *args, **kwargs):
        """
        获取订单列表 (Get order list)
        在这里，get_queryset() 已经被 DataScopeMixin 重写，
        所以查出来的 queryset 已经根据当前用户的 data_scope 进行了过滤。
        (Here, get_queryset is overridden by DataScopeMixin, 
        so the queryset is automatically filtered based on user's data_scope)
        """
        # queryset = self.filter_queryset(self.get_queryset())
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        
        # 仅为演示返回一段提示文字 (Just for demonstration)
        return Response({
            "message": "Data filtered successfully by DataScopeMixin",
            "applied_scope": request.user.get_max_data_scope() if request.user.is_authenticated else "None"
        })
