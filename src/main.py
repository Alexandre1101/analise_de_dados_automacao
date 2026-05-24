import os
from pathlib import Path
from dotenv import load_dotenv
from data_processing import load_data, process_data
from report import generate_report, generate_pdf
from email_sender import send_email

def main():
    # Obtém o caminho da pasta onde o main.py está (src) e sobe um nível para a raiz do projeto
    base_path = Path(__file__).parent.parent

    # Carrega as variáveis do arquivo .env localizado na raiz
    load_dotenv(dotenv_path=base_path / ".env")

    file_path = base_path / "data" / "vendas_semanais_ficticias.csv"

    df = load_data(str(file_path))  
    df_clean, metrics = process_data(df)
    total_vendido_no_periodo= metrics["total_vendido"]
    produto_que_mais_vendeu = df_clean.groupby("product")["total_worth"].sum().sort_values(ascending=False).index[0]
    categoria_que_mais_vendeu = df_clean.groupby("category")["total_worth"].sum().sort_values(ascending=False).index[0]
    regiao_que_mais_vendeu = df_clean.groupby("region")["total_worth"].sum().sort_values(ascending=False).index[0]
    vendedor_que_mais_vendeu = df_clean.groupby("sales_rep")["total_worth"].sum().sort_values(ascending=False).index[0]
    
    report_path = generate_report(df_clean, metrics)
    pdf_path = generate_pdf(df_clean, metrics)

    send_email(
        to=os.getenv("EMAIL_RECEIVER"),
        subject="Relatório de Vendas",
        body=f"""
Segue o relatório automático em anexo.

Resumo do período:
- Total vendido: R$ {total_vendido_no_periodo:,.2f}
- Produto com maior receita: {produto_que_mais_vendeu}
- Categoria líder: {categoria_que_mais_vendeu}
- Região com maior faturamento: {regiao_que_mais_vendeu}
- Melhor vendedor: {vendedor_que_mais_vendeu}

Relatório anexado automaticamente.
""",
        attachment=[report_path, pdf_path]
        
    )

if __name__ == "__main__":
    main()