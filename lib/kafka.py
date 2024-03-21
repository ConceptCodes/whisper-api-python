from confluent_kafka import Producer, Consumer
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
        self.consumer = Consumer(
            {'bootstrap.servers': app_config.KAFKA_BOOTSTRAP_SERVERS,
             'group.id': app_config.KAFKA_GROUP_ID,
             'auto.offset.reset': 'earliest'}
        )

    def health_check(self):
        try:
            logger.debug("Checking kafka connection")
            self.producer.list_topics(timeout=5)
            logger.debug("Kafka connection successful")
            return True
        except:
            logger.error("Kafka connection failed")
            return False
        
    def send_message(self, message):
      logger.info(f"Sending message to {app_config.KAFKA_TOPIC}: {message}")
      self.producer.produce(app_config.KAFKA_TOPIC, message)
      self.producer.flush()
      logger.info("Message sent")

    def start_consumer(self, on_message):
        self.consumer.subscribe([app_config.KAFKA_TOPIC])

        try:
            while True:
                msg = self.consumer.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    logger.error(f"Consumer error: {msg.error()}")
                    continue

                message = msg.value().decode('utf-8')
                on_message(message)

        except KeyboardInterrupt:
            pass

        finally:
            self.consumer.close()



kafka_client = Kafka()
