import pandas as pd
import numpy as np
from pathlib import Path

FEATURES = [
    "GDP per capita",
    "Social support",
    "Healthy life expectancy",
    "Freedom",
    "Generosity",
    "Perceptions of corruption",
]

def load_happiness_data(data_dir="data"):
    data_dir = Path(data_dir)
    path = data_dir / "happiness_cleaned.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} was not found. Run the cleaning step in notebooks/analysis.ipynb "
            "or place the supplied yearly CSV files in data/."
        )
    df = pd.read_csv(path)
    return df

def get_yearly_summary(df):
    return (
        df.groupby("Year", as_index=False)
          .agg(Average_Score=("Score", "mean"),
               Highest_Score=("Score", "max"),
               Lowest_Score=("Score", "min"),
               Countries=("Country", "nunique"))
          .round(3)
    )

def get_top_countries(df, year, n=10):
    return (
        df[df["Year"] == year]
        .sort_values("Rank")
        .head(n)[["Country", "Rank", "Score"]]
    )

def get_correlations(df):
    cols = ["Score"] + FEATURES
    return df[cols].corr(numeric_only=True)["Score"].drop("Score").sort_values(ascending=False)

def filter_data(df, years=None, countries=None):
    out = df.copy()
    if years:
        out = out[out["Year"].isin(years)]
    if countries:
        out = out[out["Country"].isin(countries)]
    return out
