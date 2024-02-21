from fastapi import FastAPI
from v1.endpoints import health

class APIRouter:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(APIRouter, cls).__new__(cls, *args, **kwargs)
      return cls._instance
  
  def __init__(self):
    self.api = FastAPI()

    # Health check endpoint
    self.api.include_router(health.router)


api = APIRouter().api
        