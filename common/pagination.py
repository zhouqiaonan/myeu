from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    # 英文: Default page size
    # 中文: 默认分页大小
    page_size = 10
    # 英文: URL parameter name for page size
    # 中文: 用于控制分页大小的 URL 参数名
    page_size_query_param = 'page_size'
    # 英文: Maximum page size
    # 中文: 最大分页大小
    max_page_size = 100

    def get_paginated_response(self, data):
        # 英文: Custom pagination response format
        # 中文: 自定义分页响应格式
        return Response({
            'code': 200,
            'message': 'success',
            'data': {
                'total': self.page.paginator.count,
                'page': self.page.number,
                'page_size': self.get_page_size(self.request),
                'results': data
            }
        })
