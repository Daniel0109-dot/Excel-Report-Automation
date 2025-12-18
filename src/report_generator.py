# src/report_generator.py
import os
from .text_utils import safe_filename

def generate_reports(df, output_path, mapping):
    grouped_data = {}

    for output_name, diretorias in mapping.items():
        diretorias_lower = [d.lower() for d in diretorias]
        subset = df[df["DIRETORIA"].str.lower().isin(diretorias_lower)]
        if not subset.empty:
            grouped_data[output_name] = subset

    for name, data in grouped_data.items():
        filename = safe_filename(name)
        path = os.path.join(output_path, f"Rascunho - {filename}.xlsx")
        data.to_excel(path, index=False)
