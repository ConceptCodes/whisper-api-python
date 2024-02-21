import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
      return cls._instance

  def __init__(self):
    self.MAX_FILES_FOR_USER = int(os.getenv("MAX_FILES_FOR_USER"))
    self.MAX_FILE_SIZE_IN_GB = float(os.getenv("MAX_FILE_SIZE_IN_GB"))
    self.MAX_THREADS = int(os.getenv("MAX_THREADS"))

    self.PORT= int(os.getenv("PORT"))

    self.DB_HOST = os.getenv("DB_HOST")
    self.DB_NAME = os.getenv("DB_NAME")
    self.DB_USER = os.getenv("DB_USER")
    self.DB_PASSWORD = os.getenv("DB_PASSWORD")

    self.SECRET_KEY = os.getenv("SECRET_KEY")
    self.ALGORITHM = os.getenv("ALGORITHM")
    self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

app_config = Config()
