import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

os.chdir(os.path.dirname(__file__))

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = ""
smtp_password = ""

recipients = ["computerclub@kec.edu.np"]


subject = "Mail using HTML and attached image"

with open("body.html", "r", encoding='utf-8') as f:
    body = MIMEText(f.read(),'html')


with open("fb.png","rb") as f:
    image = MIMEImage(f.read())


message = MIMEMultipart()
message.attach(body)
message.attach(image)
message['Subject'] = subject
message['From'] = smtp_username
message['TO'] = ','.join(recipients)

with smtplib.SMTP(smtp_server,smtp_port) as server:
    server.starttls()
    server.login(smtp_username,smtp_password)
    for recepient in recipients:
        server.sendmail(smtp_username,recepient,message.as_string())
        print(f"Email sent to {recepient}")

print("Done!")