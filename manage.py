#!/usr/bin/env python
# manage.py
# 英文: Django's command-line utility for administrative tasks.
# 中文: Django 用于管理任务的命令行工具。
import os
import sys

def main():
    # 英文: Run administrative tasks.
    # 中文: 运行管理任务。
    # 英文: Default to development settings, change to production in production environment.
    # 中文: 默认使用开发环境配置，在生产环境中需更改为生产配置。
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            # 英文: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable?
            # 中文: 无法导入 Django。您确定它已安装并在您的 PYTHONPATH 环境变量中可用吗？
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
