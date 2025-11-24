import os
from kafka.admin import KafkaAdminClient, NewTopic

bootstrap = os.getenv("KAFKA_BOOTSTRAP", "localhost:9094")

admin = KafkaAdminClient(bootstrap_servers=bootstrap, client_id="setup")
try:
    admin.create_topics([
        NewTopic(name="corridas", num_partitions=3, replication_factor=1)
    ])
    print("Tópico 'corridas' criado.")
except Exception as e:
    print("Aviso:", e)
finally:
    admin.close()