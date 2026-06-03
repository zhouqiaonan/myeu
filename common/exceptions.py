from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    # 英文: Call REST framework's default exception handler first, to get the standard error response.
    # 中文: 首先调用 REST framework 的默认异常处理程序，以获取标准的错误响应。
    response = exception_handler(exc, context)

    # 英文: If response is not None, it means DRF handled the exception. We can customize the format here.
    # 中文: 如果 response 不为 None，说明 DRF 处理了该异常。我们可以在这里自定义格式。
    if response is not None:
        custom_data = {
            'code': response.status_code,
            'message': 'Error occurred',
            'data': response.data
        }
        response.data = custom_data

    return response
