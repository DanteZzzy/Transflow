import os, json, redis
from dotenv import load_dotenv
from database.mongo_client import mongo_db

load_dotenv()

# ------------------ REDIS ------------------
def get_redis():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=int(os.getenv("REDIS_DB", 0)),
        decode_responses=True
    )

r = get_redis()
MOTORISTAS_SET = "motoristas"


def registrar_motorista(motorista: str):
    r.sadd(MOTORISTAS_SET, motorista)

def incrementar_saldo(motorista: str, valor: float):
    registrar_motorista(motorista)
    r.incrbyfloat(f"saldo:{motorista}", valor)

def ler_saldos():
    mts = sorted(r.smembers(MOTORISTAS_SET))
    return {m: float(r.get(f"saldo:{m}") or 0) for m in mts}

# ------------------ MONGO ------------------

def salvar_corrida(evento: dict):
    mongo_db.corridas.insert_one(evento)

def ler_corridas_mongo():
    return list(mongo_db.corridas.find({}, {"_id": 0}))