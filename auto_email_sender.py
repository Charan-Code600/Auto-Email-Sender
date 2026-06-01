


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from getpass import getpass
import os

print("=" * 50)
print("        AUTO EMAIL SENDER PRO")
print("=" * 50)

sender_email = input("Enter Sender Email: ")
app_password = getpass("Enter App Password: ")
receivers = [email.strip() for email in input("Enter Receiver Emails (comma separated): ").split(",")]
subject = input("Enter Subject: ")
print("\nWrite your message:")
message = input("> ")
attachment_path = input("Attachment Path (leave blank if none): ")

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ", ".join(receivers)
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

if attachment_path.strip():
    if not os.path.exists(attachment_path):
        print("\n❌ File not found!")
        exit()
    try:
        filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)
    except Exception as e:
        print("\n❌ Attachment Error:", e)
        exit()

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receivers, msg.as_string())
    server.quit()
    print("\n✅ Email Sent Successfully!")

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write(f"To: {', '.join(receivers)}\n")
        file.write(f"Subject: {subject}\n")
        file.write(f"Message: {message}\n")
        if attachment_path.strip():
            file.write(f"Attachment: {attachment_path}\n")
    print("📄 Email saved in history.txt")

except smtplib.SMTPAuthenticationError:
    print("\n❌ Invalid Email or App Password!")
except Exception as e:
    print("\n❌ Error:", e)
