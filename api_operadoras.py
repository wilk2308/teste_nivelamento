from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware  # Importando CORSMiddleware
import pandas as pd
from typing import List

app = FastAPI()

# Adicionar o middleware CORS para permitir requisições do front-end
origins = [
    "http://localhost:8080",  # Permitir o Vue.js rodando localmente
    "http://127.0.0.1:8080",  # Caso use o 127.0.0.1
]

# Configurar o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite acesso apenas de localhost:8080
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Carregar o CSV
CSV_PATH = "dados/Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, dtype=str, delimiter=';')

@app.get("/buscar")
def buscar_operadoras(q: str = Query(..., title="Termo de busca")) -> List[dict]:
    """Busca operadoras pelo nome ou outros campos."""
    resultado = df[df.apply(lambda row: row.astype(str).str.contains(q, case=False, na=False).any(), axis=1)]
    return resultado.to_dict(orient="records")

# Rodar com: uvicorn api_busca_operadoras:app --reload
