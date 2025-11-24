import os, json
import pika
from kafka import KafkaProducer
from dotenv import load_dotenv
from models.corrida_model import CorridaEvento

load_dotenv()

RABBIT_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
RABBIT_QUEUE = os.getenv("RABBITMQ_QUEUE", "corridas")
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "corridas")

producer = None
channel = None

def get_kafka_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_BOOTSTRAP],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
    return producer

def get_rabbit_channel():
    global channel
    if channel is None:
        conn = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))
        ch = conn.channel()
        ch.queue_declare(queue=RABBIT_QUEUE, durable=True)
        channel = ch
    return channel

def publicar_evento(evt: CorridaEvento):
    payload = evt.asdict()

    # Kafka
    producer = get_kafka_producer()
    producer.send(KAFKA_TOPIC, value=payload)

    # RabbitMQ
    channel = get_rabbit_channel()
    channel.basic_publish(
        exchange="",
        routing_key=RABBIT_QUEUE,
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2)
    )

    print("📤 Publicado:", payload)
