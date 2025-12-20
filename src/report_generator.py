# src/report_generator.py
import os
from .text_utils import safe_filename
from .config import DATA_HOJE

def generate_reports(df, output_path, mapping):
    os.makedirs(output_path, exist_ok=True)
    
    for output_name, diretorias in mapping.items():
        diretorias_lower = [d.lower() for d in diretorias]

        subset = df[
            df["DIRETORIA"]
            .astype(str)
            .str.lower()
            .isin(diretorias_lower)
        ]

        if subset.empty:
            continue

        filename = safe_filename(output_name)
        path = os.path.join(
            output_path,
            f"{filename} - {DATA_HOJE}.xlsx"
        )

        subset.to_excel(path, index=False)
