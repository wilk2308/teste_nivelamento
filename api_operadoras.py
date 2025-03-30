from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List

app = FastAPI()

# Permitir locais fixos e qualquer domínio do Vercel
fixed_origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://teste-nivelamento.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    """Middleware para adicionar CORS dinamicamente"""
    response = await call_next(request)
    origin = request.headers.get("origin")

    # Permitir qualquer subdomínio do Vercel + locais fixos
    if origin and (origin.endswith(".vercel.app") or origin in fixed_origins):
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        response.headers["Access-Control-Allow-Credentials"] = "true"

    return response

# Carregar o CSV
CSV_PATH = "dados/Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, dtype=str, delimiter=';')

@app.get("/buscar")
def buscar_operadoras(q: str = Query(..., title="Termo de busca")) -> List[dict]:
    """Busca operadoras pelo nome ou outros campos."""
    resultado = df[df.apply(lambda row: row.astype(str).str.contains(q, case=False, na=False).any(), axis=1)]
    return resultado.to_dict(orient="records")

# Rodar com: uvicorn api_operadoras:app --reload
