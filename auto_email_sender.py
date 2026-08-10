




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from getpass import getpass
import os

print("""

********************************************************
        ╔══════════════════════════════════╗
        ║      AUTO EMAIL SENDER PRO       ║
        ╚══════════════════════════════════╝
********************************************************

""")

def get_receivers():
    """Takes comma-separated emails, strips whitespace, and removes empty entries."""
    while True:
        raw = input("Enter Receiver Emails (comma separated): ")
        receivers = [email.strip() for email in raw.split(",") if email.strip()]
        if receivers:
            return receivers
        print("❌ Please enter at least one valid email address.")


def get_multiline_message():
    """Takes a multi-line message; user types 'END' on its own line to finish."""
    print("\nWrite your message (type END on a new line when done):")
    lines = []
    while True:
        line = input("> ")
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


sender_email = input("Enter Sender Email: ")
app_password = getpass("Enter App Password: ")

while True:
    print("-" * 36)
    receivers = get_receivers()
    subject = input("Enter Subject: ")
    message = get_multiline_message()
    attachment_path = input("Attachment Path (leave blank if none): ").strip()

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(receivers)
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    print("-" * 36)
    attachment_failed = False
    if attachment_path:
        if not os.path.exists(attachment_path):
            print("❌ File not found! Sending without attachment.")
            attachment_failed = True
        else:
            try:
                filename = os.path.basename(attachment_path)
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={filename}")
                msg.attach(part)
                print(f"📎 Attachment ready: {filename}")
            except Exception as e:
                print("❌ Attachment Error:", e)
                attachment_failed = True

    print("📤 Sending email...")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receivers, msg.as_string())
        server.quit()

        print("-" * 36)
        print("✅ Email Sent Successfully!")
        print(f"📬 To: {', '.join(receivers)}")
        print(f"📝 Subject: {subject}")
        print("-" * 36)

        with open("history.txt", "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 50 + "\n")
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"To: {', '.join(receivers)}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Message: {message}\n")
            if attachment_path and not attachment_failed:
                file.write(f"Attachment: {attachment_path}\n")
        print("📄 Email saved in history.txt")

    except smtplib.SMTPAuthenticationError:
        print("-" * 36)
        print("❌ Invalid Email or App Password!")
        print("-" * 36)
    except Exception as e:
        print("-" * 36)
        print("❌ Error:", e)
        print("-" * 36)

    again = input("\nSend another email? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n👋 Thank you for using Auto Email Sender Pro!")
        break





