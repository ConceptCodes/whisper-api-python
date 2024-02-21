import uvicorn
from fastapi import FastAPI 
from v1.api import api as v1_api
from lib.log import logger

if __name__ == "__main__":
    logger.info("Starting server... ")

    api = FastAPI()
    api.include_router(v1_api, prefix="/v1")

    uvicorn.run(api, host="0.0.0.0", port=80)
