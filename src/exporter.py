import pandas as pd
from pathlib import Path

def export_to_excel(df: pd.DataFrame, out_path: Path):
    df.to_excel(out_path)

def export_to_csv(df: pd.DataFrame, out_path: Path):
    df.to_csv(out_path)
