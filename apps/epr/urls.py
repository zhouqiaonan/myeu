from django.urls import path
from . import views

# 英文: App name for namespace
# 中文: 用于命名空间的 App 名称
app_name = 'epr'

# 英文: URL patterns for EPR module
# 中文: EPR 模块的路由规则
urlpatterns = [
    # 英文: Map the config URL to the EprConfigAPIView
    # 中文: 将 config 路由映射到 EprConfigAPIView
    path('configs/', views.EprConfigAPIView.as_view(), name='config-list'),
]