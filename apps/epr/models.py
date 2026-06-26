from django.db import models
from common.models import BaseModel
from products.models import ProductItem

from django.utils.translation import gettext_lazy as _

# 英文: Create your models here.
# 中文: 在这里创建你的模型。

class Territory(BaseModel):
    name_en = models.CharField(max_length=255)
    name_cn = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'territory'

class Currency(BaseModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'currency'


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


class EPRType(BaseModel):
    """
    EPR type model EPR type table - EPR 类型表
    """
    name_short_en = models.CharField(max_length=50, help_text=_("name short en"))
    name_short_cn = models.CharField(max_length=50, help_text=_("name short cn"))
    name_en = models.CharField(max_length=255, help_text=_("name en"), unique=True)
    name_cn = models.CharField(max_length=255, help_text=_("name cn"))

    def __str__(self):
        return f"{self.name_short_en} / {self.name_short_cn}"

    class Meta:
        verbose_name = _("EPR type")
        verbose_name_plural = _("EPR type")
        app_label = 'epr'
        db_table = 'epr_types'


class EPRCodeSource(BaseModel):
    """
    EPR Code Source Model - EPR Code Source Table - EPR 代码来源表
    """
    is_defined_by_law = models.BooleanField(default=False, help_text=_("is defined by law"))
    org_name_short = models.CharField(max_length=100, blank=True, null=True, help_text=_("org name short"))
    org_name = models.CharField(max_length=255, blank=True, null=True, help_text=_("org name"))

    type_in_territory = models.ForeignKey(
        'EPRTypesInTerritories',
        on_delete=models.CASCADE,
        related_name='code_sources'
    )

    def __str__(self):
        return f"{self.org_name or self.org_name_short or 'Unknown'} - {'Law' if self.is_defined_by_law else 'Other'}"

    class Meta:
        verbose_name = _("EPR Code Source")
        verbose_name_plural = _("EPR Code Source")
        unique_together = ('is_defined_by_law', 'org_name','org_name_short','type_in_territory')
        app_label = 'epr'
        db_table = 'epr_code_sources'


class EPRTypesInTerritories(BaseModel):
    """
    EPR type in territory model - The association of geography with EPR type - 地域与 EPR 类型的关联
    """
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE, related_name="territory", verbose_name=_("Territory"))
    epr_type = models.ForeignKey(EPRType, on_delete=models.CASCADE, related_name="epr_type", verbose_name=_("EPR Type"))

    class Meta:
        unique_together = ('territory', 'epr_type')
        verbose_name = _("EPR Type in Territory")
        verbose_name_plural = _("EPR Type in Territory")
        app_label = 'epr'
        db_table = 'epr_types_in_territories'

    def __str__(self):
        return f"{self.territory} - {self.epr_type}"


class EPRCode(BaseModel):
    """
    EPR code model - EPR code - EPR 代码表
    """

    MEASURING_UNIT_CHOICES = [
        (1, _('per_piece')),
        (2, _('Weight_kg')),
        (3, _('Volume_m3')),
    ]

    epr_code_source = models.ForeignKey(
        'EPRCodeSource',
        on_delete=models.CASCADE,
        related_name='epr_codes'
    )

    code = models.CharField(max_length=255, help_text=_("code"))
    description_en = models.TextField(blank=True, null=True, help_text=_("description en"))
    description_cn = models.TextField(blank=True, null=True, help_text=_("description cn"))
    description_native = models.TextField(blank=True, null=True, help_text=_("description native"))
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text=_("fee"))
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True, help_text=_("currency"))
    measuring_unit = models.IntegerField(choices=MEASURING_UNIT_CHOICES, default=1, help_text=_("measure unit"))

    def __str__(self):
        return f"{self.code} - {self.epr_code_source}"

    class Meta:
        verbose_name = _("EPR Code")
        verbose_name_plural = _("EPR Code")
        app_label = 'epr'
        db_table = 'epr_codes'


class EPRTemplate(BaseModel):
    """
    EPR template model - EPR template - EPR 模板表
    """
    name_en = models.CharField(max_length=255, help_text=_("name en"), unique=True)
    name_cn = models.CharField(max_length=255, help_text=_("name cn"))
    description_en = models.TextField(blank=True, null=True, help_text=_("description en"))
    description_cn = models.TextField(blank=True, null=True, help_text=_("description cn"))
    last_confirmed_date = models.DateField(null=True, blank=True, help_text=_("last confirmed date"))
    is_active = models.BooleanField(default=True, help_text=_("is active"))

    def __str__(self):
        return f"{self.name_en} / {self.name_cn}"

    class Meta:
        verbose_name = _("EPR Template")
        verbose_name_plural = _("EPR Template")
        app_label = 'epr'
        db_table = 'epr_templates'
        permissions = [
            ('assign_eprtemplate', 'Can assign products to EPR template'),
        ]


class Territory2EPRTemplate(BaseModel):
    """
    intermediate table - 中间表
    """
    code = models.ForeignKey(EPRCode, on_delete=models.CASCADE, related_name="territory_template_links", verbose_name=_("Code"))
    template = models.ForeignKey(EPRTemplate, on_delete=models.CASCADE, related_name="template", verbose_name=_("Template"))

    weight_override = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, help_text=_("weight override"))

    class Meta:
        unique_together = ('template', 'code')
        verbose_name = _("Intermediate Table")
        verbose_name_plural = _("Intermediate Table")
        app_label = 'epr'
        db_table = 'epr_territory_templates'

    def __str__(self):
        return f"{self.template} - {self.code}"


class EPRBatteryChemicalType(BaseModel):
    name_en = models.CharField(max_length=255, unique=True)
    name_cn = models.CharField(max_length=255)

    product_items = models.ManyToManyField(
        'products.ProductItem',
        through='EPRBatteryProductItemRelation',
        related_name='battery_chemical_types',
        blank=True,
    )

    def __str__(self):
        return f"{self.name_en} / {self.name_cn}"

    class Meta:
        verbose_name = _("EPR Battery Chemical Type")
        verbose_name_plural = _("EPR Battery Chemical Type")
        app_label = 'epr'
        db_table = 'epr_battery_chemical_types'


class EPRBatteryProductItemRelation(models.Model):
    battery_chemical_type = models.ForeignKey(
        EPRBatteryChemicalType,
        on_delete=models.PROTECT,
        related_name='product_item_relations',
        verbose_name=_("Battery Chemical Type"),
    )

    product_item = models.ForeignKey(
        'products.ProductItem',
        on_delete=models.PROTECT,
        related_name='battery_chemical_relations',
        verbose_name=_("Product Item"),
    )

    weight_kg = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        null=False,
        blank=False,
        verbose_name=_("Weight (kg)"),
        help_text=_("Weight in kg, precision 0.001 kg"),
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name=_("Quantity"),
    )

    class Meta:
        verbose_name = _("Battery Chemical–Item Relation")
        verbose_name_plural = _("Battery Chemical–Item Relations")
        app_label = 'epr'
        db_table = 'epr_battery_product_item_relations'
        unique_together = [['battery_chemical_type', 'product_item']]
