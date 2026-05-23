import yagmail

def send_email(to, subject, body, attachment):
    yag = yagmail.SMTP("seu_email@gmail.com", "senha_app")
    yag.send(to=to, subject=subject, contents=body, attachments=attachment)