import os
import smtplib
from email.mime.text import MIMEText

os.chdir(os.path.dirname(__file__))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = ''
smtp_password = ''

recipients = ["kec@yopmail.com","kantipur@yopmail.com"]



subject = "Test Email"
body = "This is a test email sent!"
message = MIMEText(body,"plain")
message['Subject'] = subject
message['From'] = smtp_username
message['To'] = ",".join(recipients)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username,smtp_password)
    for recipient in recipients:
        server.sendmail(smtp_username,recipient,message.as_string())
        print(f"Email sent to {recipient}")

print("Done!")