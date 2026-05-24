import pandas as pd
from typing import Any

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def process_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    # Encadeamos a remoção de nulos e duplicatas em um novo DataFrame
    df_processed = df.dropna().drop_duplicates().copy()
    
    # Tratando datas
    df_processed["date"] = pd.to_datetime(
        df_processed["date"],
        errors="coerce"
    )

    # Tratando números
    df_processed["price"] = pd.to_numeric(
        df_processed["price"],
        errors="coerce"
    )

    df_processed["quantity"] = pd.to_numeric(
        df_processed["quantity"],
        errors="coerce"
    )
    # Tratando texto da região
    df_processed["region"] = (
        df_processed["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.lower()
        .str.title()
    )
        # Remove duplicatas
    df_processed = df_processed.drop_duplicates()

    # Remove apenas linhas críticas
    df_processed = df_processed.dropna(
        subset=["date", "product", "price", "quantity"]
    )

    # Remove valores inválidos
    df_processed = df_processed[
        (df_processed["price"] > 0) &
        (df_processed["quantity"] > 0)
    ]
    # Nova coluna
    df_processed["total_worth"] = (
        df_processed["price"] *
        df_processed["quantity"]
    )
    total_vendido_no_periodo = df_processed["total_worth"].sum()
    produto_mais_vendido_por_receita = df_processed.groupby("product")["total_worth"].sum().sort_values(ascending=False)
    categoria_que_vendeu_mais = df_processed.groupby("category")["total_worth"].sum().sort_values(ascending=False)
    regiao_que_mais_vendeu = df_processed.groupby("region")["total_worth"].sum().sort_values(ascending=False)
    sales_rep_que_mais_vendeu = df_processed.groupby("sales_rep")["total_worth"].sum().sort_values(ascending=False)

    metrics = {
        "total_vendido": total_vendido_no_periodo,
        "produto_top": produto_mais_vendido_por_receita,
        "categoria_top": categoria_que_vendeu_mais,
        "regiao_top": regiao_que_mais_vendeu,
        "vendedor_top": sales_rep_que_mais_vendeu
    }
    return df_processed, metrics


    
