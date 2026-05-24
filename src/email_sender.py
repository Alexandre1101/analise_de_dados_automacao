import smtplib
import os
from email.message import EmailMessage

def send_email(to, subject, body, attachment=None):
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    if not email_user or not email_pass:
        raise ValueError("Erro: Credenciais de e-mail (EMAIL_USER/EMAIL_PASS) não encontradas no ambiente.")

    msg = EmailMessage()
    msg["From"] = email_user
    msg["To"] = to
    msg["Subject"] = subject

    msg.set_content(body)

    # 📎 Anexos (se existirem)
    if attachment:
        # Se for um único caminho (string ou Path), transforma em lista para iterar uniformemente
        files = [attachment] if isinstance(attachment, (str, os.PathLike)) else attachment

        for file_path in files:
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )

    # 📡 Enviar email via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_user, email_pass)
        smtp.send_message(msg)

    print("Email enviado com sucesso!")