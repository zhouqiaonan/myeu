from django.db import models
from apps.users.models import User, Department
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    """
    业务表示例：订单表 (Business Table Example: Order Model)
    对应 ER 图中的 business_table 概念。
    (Corresponds to the 'business_table' concept in the ER diagram)
    """
    order_number = models.CharField(max_length=50, unique=True, verbose_name=_("订单号 (Order Number)"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("金额 (Amount)"))
    
    # 关键字段 1：记录是谁创建了这条数据 / Key Field 1: Records who created this data
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name=_("创建人 (Created By)"))
    
    # 关键字段 2：记录这条数据是在哪个部门上下文下创建的 / Key Field 2: Records under which department context this data was created
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='orders', verbose_name=_("所属部门 (Department)"))
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "biz_order"
        verbose_name = _("订单 (Order)")

    def __str__(self):
        return self.order_number
