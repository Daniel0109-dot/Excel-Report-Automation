# src/text_utils.py
import re
import unicodedata

def normalize_text(s: str) -> str:
    if s is None:
        return ""
    s = str(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.strip().lower()

def safe_filename(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "-", name).strip()
