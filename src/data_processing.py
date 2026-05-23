import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def explore_data(df: pd.DataFrame):
    print("\nINFO GERAL:")
    print(df.info())

    print("\nVALORES NULOS:")
    print(df.isnull().sum())

    print("\nESTATÍSTICAS:")
    print(df.describe(include="all"))