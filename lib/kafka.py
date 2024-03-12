from confluent_kafka import Producer, Consumer, KafkaException
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
        self.consumer = Consumer({
            'bootstrap.servers': app_config.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': app_config.KAFKA_GROUP_ID,
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([app_config.KAFKA_TOPIC])

    def send_message(self, topic, message):
        logger.info(f"Sending message to {topic}: {message}")
        self.producer.produce(topic, message)
        self.producer.flush()

    def receive_message(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                else:
                    return msg.value().decode('utf-8')
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()


kafka_client = Kafka()
