from pydantic import BaseModel, Field
from uuid import uuid4
from time import time

class CorridaEvento(BaseModel):
    id_corrida: str = Field(default_factory=lambda: str(uuid4()))
    passageiro: dict
    motorista: str
    origem: str
    destino: str
    valor_corrida: float
    forma_pagamento: str
    ts: float = Field(default_factory=time)

    def asdict(self):
        return self.model_dump()