from pathlib import Path
from data_processing import load_data, process_data
from report import generate_report
from email_sender import send_email

def main():
    # Obtém o caminho da pasta onde o main.py está (src) e sobe um nível para a raiz do projeto
    base_path = Path(__file__).parent.parent
    file_path = base_path / "data" / "vendas_semanais_ficticias.csv"

    df = load_data(str(file_path))  
    df_clean, metrics = process_data(df)
    total_vendido_no_periodo= metrics["total_vendido"]

    report_path = generate_report(df, metrics)

    send_email(
        to="[COLOQUE O EMAIL QUE VAI RECEBER AQUI]",
        subject="Relatório de Vendas",
        body=f"Segue o relatório automático em anexo, total vendido = R${total_vendido_no_periodo:.2f}",
        attachment=report_path
    )

if __name__ == "__main__":
    main()