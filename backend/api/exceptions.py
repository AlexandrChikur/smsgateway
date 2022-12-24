from rest_framework.exceptions import APIException


class BaseReportsAPIException(APIException):
    """Базовый класс для всех исключений, связанных с API."""

    default_error_code = "error_code_name"
    default_message = "error_code_name"

    def __init__(self, message=None, error_code=None, code=None, **kwargs):
        if error_code is None:
            error_code = self.default_error_code
        if message is None:
            message = self.default_message
        error_detail = {
            "error": {
                "message": message,
                "code": error_code,
                **kwargs,
            }
        }
        super().__init__(detail=error_detail, code=code)
