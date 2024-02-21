import uuid
import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from core.constants import X_REQUEST_ID_HEADER_KEY

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logging.info(f"Request [{request.get(X_REQUEST_ID_HEADER_KEY, uuid.uuid4())}]: METHOD:: {request.method} >> URL:: {request.url}")
        response = await call_next(request)
        logging.info(f"Response: STATUS:: {response.status_code}")
        return response
