import os
from dotenv import load_dotenv
import psycopg2
from config import app_config


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.connection = psycopg2.connect(
            host=app_config.DB_HOST,
            database=app_config.DB_NAME,
            user=app_config.DB_USER,
            password=app_config.DB_PASSWORD,
        )

db = Database()