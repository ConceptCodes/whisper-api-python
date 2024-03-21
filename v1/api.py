from fastapi import APIRouter
from v1.endpoints import health
from v1.endpoints import transcript
from lib.kafka import kafka_client
import consumer

class Api:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(Api, cls).__new__(cls, *args, **kwargs)
      return cls._instance
  
  def __init__(self):
    self.router = APIRouter()

    # Health check endpoint
    self.router.include_router(health.router)

    # Transcript endpoints
    self.router.include_router(transcript.router)

    # start consumer
    kafka_client.start_consumer(consumer.on_message)


api = Api()
        