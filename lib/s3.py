import boto3
from botocore.exceptions import NoCredentialsError
from core.config import app_config
from lib.logger import logger

class S3:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(S3, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.s3 = boto3.client('s3', aws_access_key_id=app_config.AWS_ACCESS_KEY,
                               aws_secret_access_key=app_config.AWS_SECRET_KEY)

    def upload_file(self, file_path, object_name=None):
        if object_name is None:
            object_name = file_path

        try:
            logger.info(f"Uploading file {file_path} to S3")
            self.s3.upload_file(file_path, app_config.S3_BUCKET_NAME, object_name)
        except NoCredentialsError:
            logger.error("No AWS credentials found")
            return False

        return True


s3_client = S3()
