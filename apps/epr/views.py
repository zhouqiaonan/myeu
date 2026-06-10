from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import EprConfigModel
from .serializers import EprConfigSerializer

# 英文: Create your views here.
# 中文: 在这里创建你的视图。

class EprConfigAPIView(APIView):
    """
    # 英文: API view for managing EPR configurations, supporting GET and POST for decoupled frontend/backend
    # 中文: 用于管理 EPR 配置的 API 视图，支持 GET 和 POST，适用于前后端分离
    """
    # 英文: Allow any user to access this view for testing purposes
    # 中文: 允许任何用户访问此视图进行测试
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        # 英文: Retrieve all active configurations
        # 中文: 获取所有启用的配置
        """
        # 英文: Backend logic: Query database
        # 中文: 后端逻辑：查询数据库
        configs = EprConfigModel.objects.filter(is_active=True, is_deleted=False)
        
        # 英文: Serialize data for the frontend
        # 中文: 为前端序列化数据
        serializer = EprConfigSerializer(configs, many=True)
        
        # 英文: Return JSON response (standard for decoupled architectures)
        # 中文: 返回 JSON 响应（前后端分离架构的标准做法）
        return Response({
            "code": 200,
            "message": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        # 英文: Create a new configuration
        # 中文: 创建新的配置
        """
        # 英文: Deserialize data from frontend request
        # 中文: 反序列化来自前端请求的数据
        serializer = EprConfigSerializer(data=request.data)
        
        # 英文: Validate and save
        # 中文: 验证并保存
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": 201,
                "message": "created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
            
        # 英文: Return validation errors
        # 中文: 返回验证错误
        return Response({
            "code": 400,
            "message": "validation failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
