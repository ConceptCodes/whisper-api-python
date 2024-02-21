from sqlmodel import SQLModel, create_engine, Session
from core.config import app_config
from lib.logger import logger

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        logger.debug("Initializing database connection: %s", app_config.DB_NAME)
        self.engine = create_engine(
            f"postgresql://{app_config.DB_USER}:{app_config.DB_PASSWORD}@{app_config.DB_HOST}/{app_config.DB_NAME}"
        )

    def get_session(self):
        with Session(self.engine) as session:
            yield session

    def health_check(self):
        try:
            logger.debug("Checking database connection")
            with Session(self.engine) as session:
                session.exec("SELECT 1")
                logger.debug("Database connection successful")
                return True
        except:
            logger.error("Database connection failed")
            return False

db = Database()