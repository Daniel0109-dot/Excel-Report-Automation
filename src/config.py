# src/config.py
from datetime import datetime
import os

DATA_FMT = "%d-%m-%Y"
DATA_HOJE = datetime.today().strftime(DATA_FMT)

PASTA_PROCESSADO = "./input"
PASTA_SAIDA = "./output/generated_reports"

os.makedirs(PASTA_SAIDA, exist_ok=True)

COLUNAS_ESSENCIAIS = [
    "código da vaga", "rap", "diretoria", "vaga", "status da vaga", "cargo",
    "estado", "cidade da vaga", "responsável", "email do recrutador(a)",
    "data de criação", "data da última modificação", "recrutador", "status gupy",
    "cidade", "data criação",
]
