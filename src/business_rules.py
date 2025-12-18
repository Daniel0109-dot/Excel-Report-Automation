# src/business_rules.py
import pandas as pd
from .text_utils import normalize_text

HUB_TO_DIRETORIA = {
    "Operações": "Diretoria de Operações",
    "Aluguel": "Diretoria de Aluguel de Carros",
    "RAC": "Diretoria de Aluguel de Carros",
    "Gestão de Frotas": "Diretoria de Gestão de Frotas",
    "Seminovos": "Diretoria de Seminovos",
    "Gente": "Diretoria de Gente",
    "RH": "Diretoria de Gente",
    "Tecnologia": "Diretoria de Tecnologia",
    "TI": "Diretoria de Tecnologia",
    "Finanças": "Diretoria de Finanças e RI",
    "RI": "Diretoria de Finanças e RI",
    "Compras": "Diretoria de Compras de Veículos",
    "Jurídico": "Diretoria Juridica",
    "Marketing": "Diretoria de Internacionalização, MKT e Franchising",
    "MKT": "Diretoria de Internacionalização, MKT e Franchising",
    "Franchising": "Diretoria de Internacionalização, MKT e Franchising",
    "Internacionalização": "Diretoria de Internacionalização, MKT e Franchising",
    "Pesados": "Diretoria Pesados, Imo E Administrativo",
    "IMO": "Diretoria Pesados, Imo E Administrativo",
    "Administrativo": "Diretoria Pesados, Imo E Administrativo",
}

def infer_diretoria_by_hub(df: pd.DataFrame) -> pd.DataFrame:
    if "hub" not in df.columns:
        return df

    if "diretoria" not in df.columns:
        df["diretoria"] = None

    mask = df["diretoria"].isna() | (df["diretoria"].astype(str).str.strip() == "")

    def infer(hub):
        if pd.isna(hub):
            return None
        hub_norm = normalize_text(hub)
        for key, value in HUB_TO_DIRETORIA.items():
            if normalize_text(key) in hub_norm:
                return value
        return None

    df.loc[mask, "diretoria"] = df.loc[mask, "hub"].apply(infer)
    return df
