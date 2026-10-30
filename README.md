




<!-- ==================== ANIMATED BANNER ==================== -->


<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0f2027,100:2c5364&height=160&section=header&text=Auto%20Email%20Sender%20Pro&fontSize=44&fontColor=FFB800&animation=scaleIn&fontAlignY=42&desc=Python%20%7C%20SMTP%20%7C%20Gmail&descSize=18&descAlignY=68" width="100%"/>
</div>


<!-- ==================== Tagline ==================== -->

<div align="center">

### A command-line tool that sends emails through Gmail with multiple recipients, file attachments and multi-line messages — built entirely with Python's standard library.



<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>




<!-- ==================== Open to Freelance Work ==================== -->

<p align="center">
    <img src="https://img.shields.io/badge/Status-Open%20to%20Freelance%20Work-brightgreen?style=for-the-badge&labelColor=1a1a2e" height="1000" />
</p>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>





















## Features

- 📩 Send to one or multiple recipients in one go (comma-separated)
- 📝 Multi-line message support — write full paragraphs, not just a single line; type `END` on its own line when finished
- 🔁 Send multiple emails in a single run — after each email, choose to send another or exit
- 📎 File attachment support — if the attachment path is missing, invalid, or a folder instead of a file, the email still sends without it (with a warning) instead of failing
- ✅ Recipient input validation — extra commas, trailing commas, and blank entries are automatically cleaned up so a stray comma never causes an error
- 📜 Every sent email is logged to `history.txt`, with the date, recipients, subject, message, and attachment (if any)
- 🔒 Secure login using a Gmail App Password — your real Gmail password is never used, and the input is hidden as you type it
- ⚠️ Clear error handling throughout — wrong password, missing files, and connection issues all show a readable message instead of crashing

## Requirements

- Python 3.x
- No external libraries needed — `smtplib`, `email.mime`, and `getpass` are all part of Python's standard library

## How to Run

```bash
python email_sender.py
```

## Gmail Setup (required before first use)

1. Go to your Google Account → **Security**
2. Turn on **2-Step Verification** (if not already on)
3. Search for **App Passwords** and generate a new one (any name works, e.g. "Python Script")
4. Copy the 16-character password Google gives you — use that in the program, **not your normal Gmail password**

## How to Use

1. Run the script and enter your Gmail address and App Password.
2. Enter one or more receiver emails, separated by commas (a trailing comma is fine and won't cause an error).
3. Enter a subject.
4. Write your message across as many lines as you like, then type `END` on its own line to finish.
5. Optionally enter a file path to attach — or leave it blank to send without one.
6. The email sends, and a record is saved to `history.txt`.
7. You'll be asked if you want to send another email — reply `yes` to keep going without restarting, or `no` to exit.

## Security Note

- Never hardcode your App Password in the script or share it publicly.
- If an App Password is ever exposed, revoke it from your Google Account and generate a new one immediately.

## Technologies Used

- Python
- smtplib
- email.mime
- getpass

## Author

**Charan Aade | Python Developer**

🔗 [GitHub](https://github.com/Charan-Code600)



