import os
from pathlib import Path
import sys

# 英文: Build paths inside the project like this: BASE_DIR / 'subdir'.
# 中文: 在项目内构建类似这样的路径：BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 英文: Add apps directory to sys.path so we can import apps directly (e.g., from users import models)
# 中文: 将 apps 目录添加到 sys.path 中，这样我们就可以直接导入 app（例如：from users import models）
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 英文: Security warning: keep the secret key used in production secret!
# 中文: 安全警告：在生产环境中，请保持用于生产的 secret key 秘密！
SECRET_KEY = 'django-insecure-default-key-for-dev'

# 英文: Application definition
# 中文: 应用定义
INSTALLED_APPS = [
    # 英文: Django built-in apps
    # 中文: Django 内置应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 英文: Third-party apps
    # 中文: 第三方应用
    'rest_framework',
    'corsheaders',

    # 英文: Local apps
    # 中文: 本地业务应用
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    # 英文: CORS Middleware should be placed as high as possible
    # 中文: CORS 中间件应该放置在尽可能高的位置
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# 英文: Password validation
# 中文: 密码验证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 英文: Internationalization
# 中文: 国际化
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# 英文: Static files (CSS, JavaScript, Images)
# 中文: 静态文件 (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# 英文: Default primary key field type
# 中文: 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 英文: Django REST Framework Global Settings
# 中文: Django REST Framework 全局配置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    # 英文: Default pagination class
    # 中文: 默认分页类
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.CustomPagination',
    'PAGE_SIZE': 10,
    
    # 英文: Custom Exception Handler
    # 中文: 自定义异常处理
    'EXCEPTION_HANDLER': 'common.exceptions.custom_exception_handler',
}

# ==============================================================================
# 英文: CELERY SETTINGS
# 中文: Celery 配置
# ==============================================================================
# 英文: Broker URL, using Redis as the message broker.
# 中文: 消息代理 URL，使用 Redis 作为消息队列。
CELERY_BROKER_URL = 'redis://localhost:6379/0'
# 英文: Result backend, using Redis to store task results.
# 中文: 结果后端，使用 Redis 存储任务执行结果。
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
# 英文: Timezone for Celery
# 中文: Celery 的时区
CELERY_TIMEZONE = TIME_ZONE
# 英文: Task serialization format
# 中文: 任务序列化格式
CELERY_TASK_SERIALIZER = 'json'
# 英文: Result serialization format
# 中文: 结果序列化格式
CELERY_RESULT_SERIALIZER = 'json'
# 英文: Accept content types
# 中文: 接受的内容类型
CELERY_ACCEPT_CONTENT = ['json']
