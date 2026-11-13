from pandas import DataFrame

def consistency_tester(df: DataFrame, columns: list[str]):
    consistency = (
        df.groupby("surveyId")[columns]
        .nunique()
    )
    
    return {
        "max_consistency": consistency.max(),
        "total_inconsistencies": (consistency > 1).sum()
    }
