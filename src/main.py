from data_processing import load_data, explore_data#, process_data
#from report import generate_report
from email_sender import send_email

def main():
    df = load_data("data/vendas_semanais_ficticias.csv")
    explore_data(df)
    #df_processed = process_data(df)

    #report_path = generate_report(df_processed)

    send_email(
        to="alexandres.nevesjr@gmail.com",
        subject="Relatório de Vendas",
        body="Segue o relatório automático em anexo.",
        #attachment=report_path
    )

if __name__ == "__main__":
    main()