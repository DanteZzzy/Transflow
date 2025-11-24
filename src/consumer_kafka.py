import os, json
from kafka import KafkaConsumer
from dotenv import load_dotenv
from common import incrementar_saldo, salvar_corrida

load_dotenv()

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9094")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "corridas")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "processadores")

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BOOTSTRAP],
    value_deserializer=lambda v: json.loads(v.decode()),
    auto_offset_reset="latest",
    group_id=KAFKA_GROUP_ID
)

print("🦾 Consumindo Kafka...")
for msg in consumer:
    evt = msg.value
    salvar_corrida(evt)
    incrementar_saldo(evt["motorista"], float(evt["valor_corrida"]))
    print("📥 Kafka:", evt)