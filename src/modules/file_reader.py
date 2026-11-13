from pandas import read_csv as pd_rc
from pandas import DataFrame

def read_csv(path: str, row_count: int | None = None) -> DataFrame:
    return pd_rc(path, nrows=row_count)
    