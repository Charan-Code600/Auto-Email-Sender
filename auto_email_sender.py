

import smtplib
from email.mime.text import MIMEText

print("=" * 40)
print("       AUTO EMAIL SENDER")
print("=" * 40)

sender_email = input("Enter Sender Email: ")
app_password = input("Enter App Password: ")

receiver_email = input("Enter Receiver Email: ")
subject = input("Enter Subject: ")

print("\nWrite your message:")
message = input("> ")

msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()

    print("\n✅ Email Sent Successfully!")

except Exception as e:
    print("\n❌ Error:", e)
