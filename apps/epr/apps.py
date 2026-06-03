from django.apps import AppConfig


class EprConfig(AppConfig):
    # 英文: Default auto field type
    # 中文: 默认自动主键类型
    default_auto_field = "django.db.models.BigAutoField"
    # 英文: App name
    # 中文: App 名称
    name = "epr"
