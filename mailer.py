import smtplib, ssl
from email.message import EmailMessage
import datetime

PORT = 465

class Mailer:
    def __init__(self, sender_email) -> None:
        self.sender_email = sender_email

    def send_email(self, content, receiver_email, password):
        message = EmailMessage()
        message.set_content(content)
        message['Subject'] = f'Prayer Times for {datetime.date.today()}'
        message['From'] = self.sender_email
        message['To'] = receiver_email


        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
            server.login(self.sender_email, password)
            server.send_message(message)