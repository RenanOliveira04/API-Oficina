from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = []


class Events(BaseModel):
    nome: str
    dono: str
    descricao: str
    data: str
    quantidase_ingressos: int
    foram_vendidos: bool
    data_validade: str


@app.get('/')
async def hello_world() -> str:
    return 'hello world'


@app.post('/event', response_model=Events)
async def criar_evento(event: Events):
    database.append(event)

    return event


@app.get('/event')
async def ler_todos_os_eventos() -> List[Events]:
    return database
