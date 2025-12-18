# src/file_loader.py
import os
import pandas as pd

def load_latest_excel(folder_path: str) -> pd.DataFrame:
    arquivos_xlsx = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".xlsx")
    ]

    if not arquivos_xlsx:
        raise FileNotFoundError(
            f"Nenhum arquivo .xlsx encontrado em: {folder_path}"
        )

    arquivos_xlsx.sort(
        key=lambda x: os.path.getmtime(os.path.join(folder_path, x)),
        reverse=True
    )

    caminho_arquivo = os.path.join(folder_path, arquivos_xlsx[0])
    return pd.read_excel(caminho_arquivo, engine="openpyxl")
