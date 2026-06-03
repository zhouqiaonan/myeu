from django.contrib import admin
from django.urls import path, include

# 英文: Global URL configurations
# 中文: 全局路由配置
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 英文: API Endpoints routed to their respective apps
    # 中文: 将 API 路由分发到各自的 App 中
    # path('api/users/', include('users.urls')),
    # path('api/products/', include('products.urls')),
    # path('api/orders/', include('orders.urls')),
]
