from django.urls import path
from . import views

# 英文: App name for namespace
# 中文: 用于命名空间的 App 名称
app_name = 'epr'

# 英文: URL patterns for EPR module
# 中文: EPR 模块的路由规则
urlpatterns = [
    # 英文: Map the index URL to the epr_index view
    # 中文: 将 index 路由映射到 epr_index 视图
    path('index/', views.epr_index, name='index'),
]