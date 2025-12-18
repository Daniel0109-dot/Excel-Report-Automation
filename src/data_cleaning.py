# src/data_cleaning.py
import pandas as pd

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [str(col).strip().lower() for col in df.columns]
    return df

def filter_essential_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    present = [col for col in columns if col in df.columns]
    df_filtered = df[present] if present else df.copy()
    df_filtered.columns = [col.upper() for col in df_filtered.columns]
    return df_filtered
