
class ApiResponse:
    def __init__(self, status: bool, message: str, data: any = None, error_code: int = None) -> None:
        self.status = status
        self.message = message
        self.data = data
        self.error_code = error_code

    def to_json(self):
        return {
            'status': self.status,
            'message': self.message,
            'data': self.data,
            'error_code': self.error_code
        }