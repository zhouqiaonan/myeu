import os
import sys
import django

# 英文: Add the project root to the Python path
# 中文: 将项目根目录添加到 Python 路径中
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# 英文: Set up Django environment
# 中文: 配置 Django 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

def run():
    # 英文: This is a standalone script that can interact with Django models.
    # 中文: 这是一个可以与 Django 模型交互的独立脚本。
    print("Environment initialized successfully. You can run custom scripts here.")
    # from users.models import User
    # users = User.objects.all()
    # print(users)

if __name__ == '__main__':
    run()
