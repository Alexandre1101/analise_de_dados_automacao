import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    # Encadeamos a remoção de nulos e duplicatas em um novo DataFrame
    df_processed = df.dropna().drop_duplicates().copy()
    
    # Aplicamos as transformações diretamente no DataFrame limpo
    df_processed["date"] = pd.to_datetime(df_processed["date"])
    df_processed["region"] = df_processed["region"].str.strip().str.lower().str.title()
    df_processed["total_worth"] = df_processed["price"] * df_processed["quantity"]
    total_vendido_no_periodo = df_processed["total_worth"].sum()
    produto_mais_vendido_por_receita = df_processed.groupby("product")["total_worth"].sum().sort_values(ascending=False)
    categoria_que_vendeu_mais = df_processed.groupby("category")["total_worth"].sum().sort_values(ascending=False)
    regiao_que_mais_vendeu = df_processed.groupby("region")["total_worth"].sum().sort_values(ascending=False)
    sales_rep_que_mais_vendeu = df_processed.groupby("sales_rep")["total_worth"].sum().sort_values(ascending=False)

    return {
    "total_vendido": total_vendido_no_periodo,
    "produto_mais_vendido": produto_mais_vendido_por_receita,
    "categoria_top": categoria_que_vendeu_mais,
    "regiao_top": regiao_que_mais_vendeu,
    "vendedor_top": sales_rep_que_mais_vendeu
}
'''  
    print(f"Categoria que mais vendeu: {categoria_que_vendeu_mais.index[0]}")
    print(f"Região que mais vendeu: {regiao_que_mais_vendeu.index[0]}")
    print(f"Produto mais vendido por receita: {produto_mais_vendido_por_receita.index[0]}")
    print(f"Total vendido no período: R${total_vendido_no_periodo:.2f}")
    print(f"Vendedor que mais vendeu: {sales_rep_que_mais_vendeu.index[0]}")
    
    print(df_processed)
'''  
    
