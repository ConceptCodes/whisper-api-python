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
    MAX_FILES_FOR_USER = os.getenv("MAX_FILES_FOR_USER")
    MAX_FILE_SIZE_IN_GB = os.getenv("MAX_FILE_SIZE_IN_GB")
    MAX_THREADS = os.getenv("MAX_THREADS")

    # Database settings
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # Authentication settings
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

app_config = Config().config
