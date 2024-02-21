from core.models.response import ApiResponseModel

def send_success_response(msg, data = None):
    return ApiResponseModel(status=True, message=msg, data=data, error_code=None)

def send_error_response(msg, error_code = None):
    return ApiResponseModel(status=False, message=msg, data=None, error_code=error_code)
