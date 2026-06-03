from .base import *

# 英文: SECURITY WARNING: don't run with debug turned on in production!
# 中文: 安全警告：在生产环境中不要开启 DEBUG！
DEBUG = True

# 英文: Allowed hosts for development
# 中文: 开发环境允许访问的主机列表
ALLOWED_HOSTS = ['*']

# 英文: Database for development (SQLite by default)
# 中文: 开发环境数据库（默认使用 SQLite）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 英文: CORS Settings for development
# 中文: 开发环境跨域配置
CORS_ALLOW_ALL_ORIGINS = True
