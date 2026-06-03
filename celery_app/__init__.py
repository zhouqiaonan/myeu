from .main import app as celery_app

# 英文: This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# 中文: 确保 Django 启动时始终导入该 app，以便 shared_task 可以使用它。
__all__ = ('celery_app',)
