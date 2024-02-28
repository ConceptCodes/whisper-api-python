from fastapi import APIRouter
from v1.endpoints import health, auth

class Api:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(Api, cls).__new__(cls, *args, **kwargs)
      return cls._instance
  
  def __init__(self):
    self.router = APIRouter(prefix="/v1")

    # Health check endpoint
    self.router.include_router(health.router)

    # Auth endpoints
    self.router.include_router(auth.router)

api = Api()
        