




# 📧 Auto Email Sender Pro

A Python tool to send emails automatically via Gmail — supports multiple recipients, file attachments, multi-line messages, and sending several emails in one session.

## Features

- 📩 Send to one or multiple recipients (comma-separated)
- 📝 Multi-line message support — write full paragraphs, not just one line
- 🔁 Send multiple emails in a single run — no need to restart the script each time
- 📎 File attachment support (email still sends even if the attachment is missing or invalid — you'll get a warning instead of a failure)
- ✅ Input validation — empty or duplicate-comma entries in the recipient list are automatically cleaned up
- 📜 Every sent email is logged to `history.txt` (date, recipients, subject, message)
- 🔒 Secure login using Gmail App Password (never your real Gmail password)
- ⚠️ Clear error handling (wrong password, missing file, network issues)

## Requirements

- Python 3.x
- No external libraries needed — `smtplib` and `email.mime` are part of Python's standard library

## How to Run

```bash
python email_sender.py
```

## Gmail Setup (required before first use)

1. Go to your Google Account → **Security**
2. Turn on **2-Step Verification** (if not already on)
3. Search for **App Passwords** and generate a new one (choose any name, e.g. "Python Script")
4. Copy the 16-character password Google gives you — use that in the program, **not your normal Gmail password**

## How to Use

1. Run the script and enter your Gmail address and App Password (the password won't be visible as you type — that's normal, it's hidden for security).
2. Enter one or more receiver emails, separated by commas.
3. Enter a subject.
4. Write your message. You can write multiple lines — type `END` on its own line when you're done.
5. Optionally enter a file path to attach a file, or leave it blank.
6. The email is sent, and a copy of the details is saved to `history.txt`.
7. You'll be asked if you want to send another email — reply `yes` to send more without restarting, or `no` to exit.

## Security Note

- Never hardcode your App Password directly in the script or share it publicly.
- If you accidentally expose an App Password, revoke it from your Google Account and generate a new one.

## Technologies Used

- Python
- smtplib
- email.mime
- getpass

## Author

Charan Aade | Python Developer






