from models import Response

def send_success_response(data, msg = None):
    return Response(True, msg, data).to_json()

def send_error_response(msg, error_code = None):
    return Response(False, msg, error_code = error_code).to_json()
