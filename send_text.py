import smtplib
import os
from email.message import EmailMessage

def text_alert(subject, body, to=None):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to or os.getenv("TO_EMAIL")
    msg['From'] = os.getenv("EMAIL_USER")
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(
            os.getenv("EMAIL_USER"),
            os.getenv("EMAIL_PASS"))
        server.send_message(msg)
        print("Sent!")
    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()  