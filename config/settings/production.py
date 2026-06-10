from .base import *
import os
from dotenv import load_dotenv

# 英文: Load environment variables from .env file
# 中文: 从 .env 文件加载环境变量
load_dotenv(os.path.join(BASE_DIR, '.env'))

# 英文: SECURITY WARNING: don't run with debug turned on in production!
# 中文: 安全警告：在生产环境中不要开启 DEBUG！
DEBUG = False

# 英文: Allow all hosts in docker (or specify your domain)
# 中文: 在 Docker 中允许所有主机访问（或指定你的域名）
ALLOWED_HOSTS = ['*']

# 英文: Database for production (PostgreSQL via Docker)
# 中文: 生产环境数据库（通过 Docker 使用 PostgreSQL）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'myeu_db'),
        'USER': os.environ.get('DB_USER', 'myeu_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'myeu_password'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# 英文: Override Celery broker to use RabbitMQ in Docker
# 中文: 覆盖 Celery 消息代理，使用 Docker 中的 RabbitMQ
CELERY_BROKER_URL = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@rabbitmq:5672//')

# 英文: Override Redis for Celery backend/cache
# 中文: 覆盖 Redis 配置（用于 Celery 结果后端或缓存）
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://redis:6379/1')

# 英文: Static files root for production (collected here for Nginx)
# 中文: 生产环境静态文件根目录（供 Nginx 收集和代理）
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 英文: CORS Settings for production (Allow all for testing, change in real production)
# 中文: 生产环境跨域配置（测试期间允许所有，实际生产请修改）
CORS_ALLOW_ALL_ORIGINS = True
