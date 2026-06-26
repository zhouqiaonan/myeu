from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _

class ProductItem(BaseModel):
    """
    Product Item - 产品项
    """
    name_en = models.CharField(max_length=255, verbose_name=_("Name EN"))
    name_cn = models.CharField(max_length=255, verbose_name=_("Name CN"))

    class Meta:
        db_table = 'product_item'
        verbose_name = _("Product Item")
        verbose_name_plural = _("Product Items")

    def __str__(self):
        return f"{self.name_en} / {self.name_cn}"
