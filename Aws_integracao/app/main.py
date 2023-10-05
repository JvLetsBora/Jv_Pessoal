from ponderada3 import prever
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/predict")
def read_root(titulo: str = Query(...), body_: str = Query(...)):
    resposta = prever({"titulo":titulo,"body_":body_})
    return resposta

