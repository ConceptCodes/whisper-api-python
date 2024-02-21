import uvicorn
from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from v1.api import api as v1_api
from lib.logger import logger
from core.config import app_config
from v1.middlewares.logging import LoggingMiddleware

if __name__ == "__main__":
    logger.info("Starting server on port %d", app_config.PORT)

    api = FastAPI()
    
    api.add_middleware(LoggingMiddleware)
    api.include_router(v1_api.router, prefix="/v1", default_response_class=JSONResponse)
    
    uvicorn.run(api, host="0.0.0.0", port=app_config.PORT, use_colors=True, timeout_graceful_shutdown=10)
