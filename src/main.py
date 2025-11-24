import os, json, asyncio
from fastapi import FastAPI, Body, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models.corrida_model import CorridaEvento
from common import ler_saldos, ler_corridas_mongo
from producer_both import publicar_evento


load_dotenv()


app = FastAPI(title="TransFlow – Corridas Assíncronas")
app.add_middleware(
CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    )


@app.get("/corridas")
async def listar_corridas():
    return ler_corridas_mongo()


@app.post("/corridas")
async def cadastrar_corrida(evt: CorridaEvento = Body(...)):
    publicar_evento(evt)
    return {"status": "publicado", "corrida": evt.asdict()}


@app.get("/saldo/{motorista}")
async def saldo_motorista(motorista: str):
    return {"motorista": motorista, "saldo": ler_saldos().get(motorista, 0)}


@app.websocket("/ws")
async def websocket_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            await ws.send_text(json.dumps({
            "saldos": ler_saldos(),
            "corridas": ler_corridas_mongo()
    }))

            await asyncio.sleep(1)
    except:
        await ws.close()