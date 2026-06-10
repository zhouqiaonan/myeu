from django.db import models
from common.models import BaseModel

# 英文: Create your models here.
# 中文: 在这里创建你的模型。

class EprConfigModel(BaseModel):
    """
    # 英文: A basic configuration model for the EPR module
    # 中文: EPR 模块的基础配置模型
    """
    name = models.CharField(max_length=100, verbose_name="配置名称 / Configuration Name")
    value = models.CharField(max_length=255, verbose_name="配置值 / Configuration Value")
    is_active = models.BooleanField(default=True, verbose_name="是否启用 / Is Active")

    class Meta:
        db_table = "epr_config"
        verbose_name = "EPR配置 / EPR Configuration"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}: {self.value}"
