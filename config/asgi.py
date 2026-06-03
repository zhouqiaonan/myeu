import os
from django.core.asgi import get_asgi_application

# 英文: Default to development settings, change to production in production environment.
# 中文: 默认使用开发环境配置，在生产环境中需更改为生产配置。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_asgi_application()
