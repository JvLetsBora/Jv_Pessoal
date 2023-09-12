from ponderada3 import predict, pepiline
from fastapi import FastAPI

app = FastAPI()

def formatar_tempo(numero):
    horas = int(numero // 3600)
    minutos = int((numero % 3600) // 60)
    segundos = int(numero % 60)
    
    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    
    return tempo_formatado

@app.post("/")
def read_root(item: dict):
    data = pepiline(item)
    resposta = int(predict(data))
    resposta = formatar_tempo(resposta)
    return {"Tempo: ": f"{resposta}"}

