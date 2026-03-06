import pandas as pd
from typing import Dict

def make_presence_table(env_lists: Dict[str, pd.Series]) -> pd.DataFrame:
    # 1. collect all unique values
    unique = pd.Index(
        pd.concat(env_lists.values()).unique()
    ).sort_values()

    # 2. build an empty DataFrame of zeros
    presence = pd.DataFrame(
        0, index=unique, columns=list(env_lists.keys())
    )

    # 3. fill in ones where appropriate
    for env, series in env_lists.items():
        presence.loc[series.unique(), env] = 1

    presence.index.name = "variable_name"
    return presence
