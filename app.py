import uvicorn
from fastapi import FastAPI 
from fastapi.responses import JSONResponse

from v1.api import api as v1_api
from v1.middlewares.logging import LoggingMiddleware
from lib.db import db
from lib.logger import logger
from core.config import app_config

def main():
  logger.info("Starting server on port %d", app_config.PORT)

  api = FastAPI()

  db.create_db_and_tables()
  
  api.add_middleware(LoggingMiddleware)
  api.include_router(v1_api.router, default_response_class=JSONResponse)
  
  # uvicorn.run(api, host="0.0.0.0", port=app_config.PORT, use_colors=True, timeout_graceful_shutdown=10)
  return api
