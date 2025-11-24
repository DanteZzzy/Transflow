# 🚕 TransFlow – Sistema de Mensageria de Corridas

Este projeto é uma API assíncrona desenvolvida com **FastAPI** que simula o fluxo de corridas de transporte, utilizando **Kafka** e **RabbitMQ** como sistemas de mensageria e **MongoDB** para persistência de dados.

---

## 📦 Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* Docker & Docker Compose
* Kafka
* RabbitMQ
* MongoDB
* Redis
* Pika
* kafka-python

---

## ⚙️ Passos de Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/transflow.git
cd transflow
```

### 2️⃣ Criar o arquivo .env

Crie um arquivo chamado `.env` na raiz do projeto (não será versionado pois está no .gitignore):

```env
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
RABBITMQ_QUEUE=transacoes
KAFKA_BOOTSTRAP=localhost:9094
KAFKA_TOPIC=transacoes
KAFKA_GROUP_ID=processadores
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
MONGO_URL=mongodb://root:example@localhost:27017
MONGO_DB=mensageria
LOG_TO_MONGO=false
APP_PORT=8000
```

### 3️⃣ Subir os containers

```bash
docker-compose up --build
```

A API ficará disponível em:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## 🔐 Variáveis de Ambiente Necessárias

| Variável        | Descrição                   |
| --------------- | --------------------------- |
| RABBITMQ_URL    | URL de conexão com RabbitMQ |
| RABBITMQ_QUEUE  | Fila utilizada              |
| KAFKA_BOOTSTRAP | Endereço do broker Kafka    |
| KAFKA_TOPIC     | Tópico de publicação        |
| KAFKA_GROUP_ID  | Grupo de consumidores       |
| MONGO_URL       | String de conexão MongoDB   |
| MONGO_DB        | Banco de dados              |
| REDIS_HOST      | Host Redis                  |
| REDIS_PORT      | Porta Redis                 |
| APP_PORT        | Porta da aplicação          |

---

## ▶️ Instruções de Uso

### Cadastrar corrida

Endpoint:

```
POST /corridas
```

Payload de exemplo:

```json
{
  "id_corrida": "CRD123",
  "passageiro": {
    "nome": "João Silva"
  },
  "motorista": "Carlos Souza",
  "origem": "Centro",
  "destino": "Rodoviária",
  "valor_corrida": 35.50,
  "forma_pagamento": "cartao",
  "ts": 1700000000
}
```

Resposta esperada:

```json
{
  "status": "publicado",
  "corrida": {...}
}
```

### Listar corridas

```
GET /corridas
```

### Consultar saldo motorista

```
GET /saldo/{motorista}
```

---

## 🧪 Testes

Você pode testar utilizando:

* ✅ Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
* ✅ Postman / Insomnia
* ✅ Curl:

```bash
curl -X POST http://localhost:8000/corridas \
-H "Content-Type: application/json" \
-d '{
  "id_corrida": "CRD123",
  "passageiro": {"nome": "Maria"},
  "motorista": "Pedro",
  "origem": "Centro",
  "destino": "Praia",
  "valor_corrida": 50.00,
  "forma_pagamento": "pix",
  "ts": 1700000000
}'
```

No terminal é esperado:

```
📤 Publicado: {...}
```

---

## 🖼️ Captura de Tela do Sistema em Execução

![alt text](<Captura de tela 2025-11-24 002518.png>)
---

## ✅ Status do Projeto

✔ API funcional
✔ Integração Kafka e RabbitMQ
✔ Persistência MongoDB
✔ Dockerizado e pronto para produção

---

## 👨‍💻 Autor

Gabriel Teixeira de Faria
Projeto acadêmico - TransFlow

---

Se quiser, posso gerar uma versão mais profissional ou mais simples do README 👍
