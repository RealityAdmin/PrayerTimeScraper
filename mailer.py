import smtplib, ssl

PORT = 465

class Mailer:
    def __init__(self, sender_email, receiver_email) -> None:
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def send_email(self, message, password):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
            server.login(self.sender_email, password)
            server.sendmail(self.send_email, self.receiver_email, message)