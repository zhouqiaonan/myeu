from django.db import models

class BaseModel(models.Model):
    # 英文: Creation time, auto set to now when object is created.
    # 中文: 创建时间，对象创建时自动设置为当前时间。
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 英文: Update time, auto set to now every time object is saved.
    # 中文: 更新时间，每次保存对象时自动设置为当前时间。
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # 英文: Logical deletion flag
    # 中文: 逻辑删除标志
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        # 英文: Declare as abstract base class, will not create a database table
        # 中文: 声明为抽象基类，不会创建数据库表
        abstract = True
