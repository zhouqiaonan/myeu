import os
from celery import Celery

# 英文: Set the default Django settings module for the 'celery' program.
# 中文: 为 'celery' 程序设置默认的 Django settings 模块。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

# 英文: Initialize Celery App
# 中文: 初始化 Celery 实例
app = Celery('myeu')

# 英文: Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 中文: 使用字符串意味着 worker 不需要将配置对象序列化到子进程中。
# namespace='CELERY' 表示所有与 Celery 相关的配置键都应该带有 `CELERY_` 前缀。
app.config_from_object('django.conf:settings', namespace='CELERY')

# 英文: Load task modules from all registered Django apps.
# 中文: 从所有已注册的 Django App 中加载任务模块。
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    # 英文: A simple debug task to verify Celery is working
    # 中文: 一个简单的调试任务，用于验证 Celery 是否正常工作
    print(f'Request: {self.request!r}')
