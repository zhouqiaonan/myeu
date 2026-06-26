from .base import *
import os
from dotenv import load_dotenv

# 英文: Load environment variables from .env file
# 中文: 从 .env 文件加载环境变量
load_dotenv(os.path.join(BASE_DIR, '.env'))

# 英文: SECURITY WARNING: don't run with debug turned on in production!
# 中文: 安全警告：在生产环境中不要开启 DEBUG！
DEBUG = True

# 英文: Allowed hosts for development
# 中文: 开发环境允许访问的主机列表
ALLOWED_HOSTS = ['*']

# 英文: Database for development (PostgreSQL via Docker on localhost)
# 中文: 开发环境数据库（连接到本地 Docker 映射的 PostgreSQL 端口）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'myeu_db'),
        'USER': os.environ.get('DB_USER', 'myeu_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'myeu_password'),
        # 本地开发时覆盖 .env 中的 db，改为连接 localhost
        'HOST': '127.0.0.1', 
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# 英文: Override Celery broker to use localhost Redis/RabbitMQ
# 中文: 开发环境使用本地映射的 Redis/RabbitMQ 端口
CELERY_BROKER_URL = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@127.0.0.1:5672//')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1')

# 英文: CORS Settings for development
# 中文: 开发环境跨域配置
CORS_ALLOW_ALL_ORIGINS = True
