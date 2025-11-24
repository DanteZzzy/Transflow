import os, json, pika
from dotenv import load_dotenv
from common import incrementar_saldo, salvar_corrida

load_dotenv()

RABBIT_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
RABBIT_QUEUE = os.getenv("RABBITMQ_QUEUE", "transacoes")

parameters = pika.URLParameters(RABBIT_URL)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=RABBIT_QUEUE, durable=True)

print("🐇 Consumer RabbitMQ aguardando mensagens...")

def callback(ch, method, properties, body):
    evt = json.loads(body.decode())

    salvar_corrida(evt)
    incrementar_saldo(evt["motorista"], float(evt["valor_corrida"]))

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("✅ RabbitMQ recebeu:", evt)

channel.basic_consume(queue=RABBIT_QUEUE, on_message_callback=callback)
channel.start_consuming()
