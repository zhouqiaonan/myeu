import sys
import os

# 英文: Ensure the project root is in sys.path so 'celery_app' can be found.
# 中文: 确保项目根目录在 sys.path 中，以便能找到 'celery_app' 模块。
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from celery_app import celery_app

# 英文: This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# 中文: 确保 Django 启动时始终导入该 app，以便 shared_task 可以使用它。
__all__ = ('celery_app',)
