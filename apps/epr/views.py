from django.shortcuts import render
from django.http import JsonResponse

# 英文: Create your views here.
# 中文: 在这里创建你的视图。

def epr_index(request):
    """
    # 英文: Basic index view for EPR module
    # 中文: EPR 模块的基础首页视图
    """
    return JsonResponse({"message": "Welcome to the EPR module API!", "status": "success"})
