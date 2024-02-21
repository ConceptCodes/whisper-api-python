import uvicorn
from v1.router import api
from lib.log import logger

if __name__ == "__main__":
    logger.info("Starting server... ")
    uvicorn.run(api, host="0.0.0.0", port=80)
