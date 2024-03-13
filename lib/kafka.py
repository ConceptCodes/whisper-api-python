from confluent_kafka import Producer
from core.config import app_config
from lib.logger import logger


class Kafka:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Kafka, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.producer = Producer(
            {'bootstrap.servers': app_config.KAFKA_BOOTSTRAP_SERVERS})

    def send_message(self, topic, message):
        logger.info(f"Sending message to {topic}: {message}")
        self.producer.produce(topic, message)
        self.producer.flush()


kafka_client = Kafka()
