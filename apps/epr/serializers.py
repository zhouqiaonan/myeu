from rest_framework import serializers
from .models import EprConfigModel


class EprConfigSerializer(serializers.ModelSerializer):
    """
    # 英文: Serializer for the EprConfigModel, converts complex querysets into native Python datatypes
    # 中文: EprConfigModel 的序列化器，负责将复杂的查询集转换为原生 Python 数据类型（以便后续转为 JSON）
    """

    class Meta:
        model = EprConfigModel
        # 英文: Include all fields in the serialization, or specify a list like ['id', 'name', 'value']
        # 中文: 序列化包含所有字段，也可以指定列表例如 ['id', 'name', 'value']
        fields = '__all__'

        # 英文: Make certain fields read-only so they cannot be modified via API
        # 中文: 将某些字段设为只读，使其不能通过 API 被修改
        read_only_fields = ('id', 'created_time', 'updated_time', 'is_deleted')