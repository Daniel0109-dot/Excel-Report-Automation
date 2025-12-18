# main.py
from src.config import (
    PASTA_PROCESSADO, PASTA_SAIDA,
    COLUNAS_ESSENCIAIS, DATA_HOJE
)
from src.file_loader import load_latest_excel
from src.data_cleaning import normalize_columns, filter_essential_columns
from src.business_rules import infer_diretoria_by_hub
from src.report_generator import generate_reports

MAPPING = {
    f"Responsavel A {DATA_HOJE}": [...],
    f"Responsavel B {DATA_HOJE}": [...],
}

def main():
    df = load_latest_excel(PASTA_PROCESSADO)
    df = normalize_columns(df)
    df = infer_diretoria_by_hub(df)
    df = filter_essential_columns(df, COLUNAS_ESSENCIAIS)
    generate_reports(df, PASTA_SAIDA, MAPPING)

if __name__ == "__main__":
    main()
