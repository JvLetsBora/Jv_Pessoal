from ponderada3 import prever
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def read_root(item: dict):
    resposta = prever(item)
    return {"Tempo: ": f"{resposta}"}

