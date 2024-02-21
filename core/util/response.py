from core.models.response import ApiReponseModel

def send_success_response(data, msg = None):
    return ApiReponseModel(status=True, message=msg, data=data)

def send_error_response(msg, error_code = None):
    return ApiReponseModel(status=False, message=msg, data=None, error_code=error_code)
