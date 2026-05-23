from pathlib import Path
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#total_vendido_no_periodo, produto_mais_vendido_por_receita, categoria_que_vendeu_mais, regiao_que_mais_vendeu, sales_rep_que_mais_vendeu

def generate_report(df, metrics):
    # Define o caminho absoluto para a pasta de saída (raiz do projeto/output)
    base_path = Path(__file__).parent.parent
    output_dir = base_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    path = str(output_dir / "relatorio.xlsx")

    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, sheet_name="dados_brutos", index=False)

        metrics["produto_top"].to_excel(writer, sheet_name="produtos_mais_vendidos")
        metrics["categoria_top"].to_excel(writer, sheet_name="categorias_mais_vendidas")
        metrics["regiao_top"].to_excel(writer, sheet_name="regioes_com_mais_vendas")
        metrics["vendedor_top"].to_excel(writer, sheet_name="vendedores_com_mais_vendas")

        

    return path