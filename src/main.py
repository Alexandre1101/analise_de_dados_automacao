import os
from pathlib import Path
from dotenv import load_dotenv
from data_processing import load_data, process_data
from report import generate_report
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

    report_path = generate_report(df_clean, metrics)

    send_email(
        to=os.getenv("EMAIL_RECEIVER"),
        subject="Relatório de Vendas",
        body=f"Segue o relatório automático em anexo, total vendido = R${total_vendido_no_periodo:.2f}",
        attachment=report_path
    )

if __name__ == "__main__":
    main()