import smtplib
from email.message import EmailMessage


def email_alert(body, to, subject):
    msg = EmailMessage()
    msg.set_content(body)

    msg["to"] = to
    msg["subject"] = subject

    user = "puru.sharingan@gmail.com"
    msg["from"] = user
    password = "iiquefjrrlgjurty"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    email_alert("Aur bhai coder", "andrewcoder08@gmail.com", "Testing")
