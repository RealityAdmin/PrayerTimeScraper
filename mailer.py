import smtplib, ssl
from email.message import EmailMessage
import datetime

PORT = 465

class Mailer:
    def __init__(self, sender_email, receiver_email) -> None:
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def send_email(self, content, password):
        message = EmailMessage()
        message.set_content(content)
        message['Subject'] = f'Prayer Times for {datetime.date.today()}'
        message['From'] = self.sender_email
        message['To'] = self.receiver_email


        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
            server.login(self.sender_email, password)
            server.send_message(message)