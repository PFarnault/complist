import pandas as pd
from pathlib import Path
from typing import Dict

def load_environment_lists(data_dir: Path) -> Dict[str, pd.Series]:
    """
    Scans data_dir for .xlsx/.xls/.csv files.
    Assumes each file is a single‐column list of animal names.
    Returns dict: { environment_name: pd.Series([...]) }
    """
    env_lists = {}
    for path in data_dir.iterdir():
        if path.suffix in {".xlsx", ".xls"}:
            # use the filename (without extension) as environment name
            env = path.stem  
            df = pd.read_excel(path, header=None, names=["variable_name"])
            env_lists[env] = df["variable_name"].dropna().astype(str).str.strip()
        elif path.suffix == ".csv":
            env = path.stem
            df = pd.read_csv(path, header=None, names=["variable_name"])
            env_lists[env] = df["variable_name"].dropna().astype(str).str.strip()
        elif path.suffix == ".dta":
            env = path.stem
            df = pd.read_stata(path, header=None, names=["variable_name"])
            env_lists[env] = df["variable_name"].dropna().astype(str).str.strip()
    return env_lists
