import os
import smtplib
import csv
from email.mime.text import MIMEText

# Change directory to the current script's directory
os.chdir(os.path.dirname(__file__))

# Email server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = ""  # Your email
smtp_password = ""         # Your email password

# Email subject
subject = "Registration Confirmation: Python Automation Workshop"

# Room number constant
room_no = "A-405"  # Assign a constant room number

# Read the HTML template
with open("apologies.html", "r", encoding='utf-8') as f:
    body_template = f.read()

# Function to send email
def send_email(to_email, name):
    body = body_template.replace("{name}", name).replace("{room_no}", room_no)
    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['From'] = smtp_username
    message['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())
        print(f"Email sent to {to_email}")

# Read the CSV file
with open('b.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        email = row['Email']
        send_email(email, name)

print("Done!")
