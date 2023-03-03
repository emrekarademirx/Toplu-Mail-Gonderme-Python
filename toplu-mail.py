import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# E-posta ayarları
sender_email = "sender@emrekarademir.com"
receiver_email = "recipient1@emrekarademir.com, recipient2@emrekarademir.com, recipient3@emrekarademir.com"
password = "sender_email_password"

# Konu ve içerik
subject = "Toplu E-posta Gönderme"
message = """
<html>
  <head>
    <title>Toplu E-posta Gönderme</title>
  </head>
  <body>
    <p>Merhaba,</p>
    <p>Bu bir toplu e-posta örneğidir.</p>
    <p>İyi günler!</p>
  </body>
</html>
"""

# Dosya eki (isteğe bağlı)
filename = "example.pdf"

# E-posta oluşturma
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "html"))

# Dosya eki ekleme (isteğe bağlı)
if filename:
    with open(filename, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)

# E-posta gönderme
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(", "), msg.as_string())
