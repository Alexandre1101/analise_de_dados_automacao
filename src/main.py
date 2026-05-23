from pathlib import Path
from data_processing import load_data, process_data
from report import generate_report
from email_sender import send_email

def main():
    # Obtém o caminho da pasta onde o main.py está (src) e sobe um nível para a raiz do projeto
    base_path = Path(__file__).parent.parent
    file_path = base_path / "data" / "vendas_semanais_ficticias.csv"

    df = load_data(str(file_path))  
    df_processed = process_data(df)
    report_path = generate_report(df_processed)
'''
    send_email(
        to="alexandres.nevesjr@gmail.com",
        subject="Relatório de Vendas",
        body="Segue o relatório automático em anexo.",
        attachment=report_path
    )'''

if __name__ == "__main__":
    main()