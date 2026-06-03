from .base import *

# 英文: SECURITY WARNING: don't run with debug turned on in production!
# 中文: 安全警告：在生产环境中不要开启 DEBUG！
DEBUG = False

# 英文: Must be set in production
# 中文: 生产环境必须设置
ALLOWED_HOSTS = ['your-production-domain.com']

# 英文: Database for production (e.g., PostgreSQL or MySQL)
# 中文: 生产环境数据库（如 PostgreSQL 或 MySQL）
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# 英文: CORS Settings for production
# 中文: 生产环境跨域配置（仅允许指定的域名访问）
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
