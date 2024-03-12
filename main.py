from fastapi import FastAPI
from fastapi.responses import JSONResponse
from v1.api import api as v1_api
from v1.middlewares.logging import LoggingMiddleware

def create_app():
    api = FastAPI()

    api.add_middleware(LoggingMiddleware)
    api.include_router(v1_api.router, prefix="/v1",
                       default_response_class=JSONResponse)

    return api

app = create_app()
