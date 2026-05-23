import smtplib
import os
from email.message import EmailMessage

def send_email(to, subject, body, attachment=None):
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg["From"] = email_user
    msg["To"] = to
    msg["Subject"] = subject

    msg.set_content(body)

    # 📎 Anexo (se existir)
    if attachment:
        with open(attachment, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment)

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