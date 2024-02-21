import logging
import json

class Logger:
  _instance = None

  def __new__(cls, *args, **kwargs):
      if not cls._instance:
          cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
      return cls._instance
  
  def __init__(self):
    self.logger = logging.getLogger("api")
    self.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)
  
logger = Logger().logger