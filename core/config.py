import os

from core.constants import MAX_FILE_SIZE_IN_GB 
from core.constants import MAX_FILES_FOR_USER
from core.constants import ACCESS_TOKEN_EXPIRE_MINUTES

class Config:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
      return cls._instance

  def __init__(self):
    self.MAX_FILES_FOR_USER = int(os.getenv("MAX_FILES_FOR_USER")) or MAX_FILES_FOR_USER
    self.MAX_FILE_SIZE_IN_GB = float(os.getenv("MAX_FILE_SIZE_IN_GB")) or MAX_FILE_SIZE_IN_GB

    self.DB_HOST = os.getenv("DB_HOST")
    self.DB_NAME = os.getenv("DB_NAME")
    self.DB_USER = os.getenv("DB_USER")
    self.DB_PORT = os.getenv("DB_PORT")
    self.DB_PASSWORD = os.getenv("DB_PASSWORD")

    self.RESEND_API_KEY = os.getenv("RESEND_API_KEY")

    self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    self.KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")
    self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

    self.SECRET_KEY = os.getenv("SECRET_KEY")
    self.ALGORITHM = os.getenv("ALGORITHM")
    self.ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) or ACCESS_TOKEN_EXPIRE_MINUTES

    self.AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    self.AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    self.S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

app_config = Config()
