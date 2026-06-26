from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('dept_roles__department', 'dept_roles__role').all()
    serializer_class = UserSerializer
    # 英文: For development purposes, allow any access
    # 中文: 开发环境下，允许任意访问（稍后可以换成实际的权限类）
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        # 英文: Standard list with pagination if configured, otherwise standard DRF response
        # 中文: 使用 DRF 标准的 list 响应，会被 CustomPagination 自动包装
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # 英文: Handle standard user creation
        # 中文: 处理标准用户创建
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # TODO: Handle deptRoles saving logic here
        
        return Response({
            "message": "User created successfully", 
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # 英文: Handle standard user update
        # 中文: 处理标准用户更新
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # TODO: Handle deptRoles updating logic here

        return Response({
            "message": "User updated successfully", 
            "data": serializer.data
        }, status=status.HTTP_200_OK)
