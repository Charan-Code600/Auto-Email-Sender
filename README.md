




<!-- ==================== ANIMATED BANNER ==================== -->


<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0f2027,100:2c5364&height=160&section=header&text=Auto%20Email%20Sender%20Pro&fontSize=44&fontColor=FFB800&animation=scaleIn&fontAlignY=42&desc=Python%20%7C%20SMTP%20%7C%20Gmail&descSize=18&descAlignY=68" width="100%"/>
</div>


<!-- ==================== Tagline ==================== -->

<div align="center">

### A command-line tool that sends emails through Gmail with multiple recipients, file attachments and multi-line messages — built entirely with Python's standard library.

</div>

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


<!-- ==================== Badges ==================== -->

<div align="center">

# $\textsf{\color{#FFB800}{Badges}}$

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None-00C851?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-2B2B2B?style=for-the-badge&logo=gnubash&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-FFB800?style=for-the-badge)

</div>



<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== Table of Contents ==================== -->

<div align="center">

#  $\textsf{\color{#FFB800}{Table of Contents}}$

</div>


<div align="center">
<table>
<tr><td align="left">

[![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)](#overview)
<br>
[![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)](#demo)
<br>
[![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)](#features)
<br>
[![4 Tech Stack](https://img.shields.io/badge/4-Tech%20Stack-FFB800?style=for-the-badge&labelColor=1a1a2e)](#tech-stack)
<br>
[![5 Installation](https://img.shields.io/badge/5-Installation-FFB800?style=for-the-badge&labelColor=1a1a2e)](#installation)
<br>
[![6 How to Use](https://img.shields.io/badge/6-How%20to%20Use-FFB800?style=for-the-badge&labelColor=1a1a2e)](#how-to-use)
<br>
[![7 Project Structure](https://img.shields.io/badge/7-Project%20Structure-FFB800?style=for-the-badge&labelColor=1a1a2e)](#project-structure)
<br>
[![8 Key Highlights](https://img.shields.io/badge/8-Key%20Highlights-FFB800?style=for-the-badge&labelColor=1a1a2e)](#key-highlights)
<br>
[![9 Future Improvements](https://img.shields.io/badge/9-Future%20Improvements-FFB800?style=for-the-badge&labelColor=1a1a2e)](#future-improvements)
<br>
[![10 Author](https://img.shields.io/badge/10-Author-FFB800?style=for-the-badge&labelColor=1a1a2e)](#author)

</td></tr>
</table>
</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Overview ==================== -->

<a id="overview"></a>

![1 Overview](https://img.shields.io/badge/1-Overview-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

### Sending similar emails again and again, to several people and with a file attached, is slow and repetitive. This project automates it from the terminal: it logs in to Gmail over SMTP using a secure App Password, builds the message with an optional attachment, sends it, and keeps a log of every email. It was built to practice working with a real network protocol, file handling and safe credential input.

</div>

<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Demo ==================== -->

<a id="demo"></a>

![2 Demo](https://img.shields.io/badge/2-Demo-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">
<i>Real output: a normal email, then an email with a missing attachment. The program warns and still sends it.</i>
</div>

```
********************************************************
        ╔══════════════════════════════════╗
        ║      AUTO EMAIL SENDER PRO       ║
        ╚══════════════════════════════════╝
********************************************************


Enter Sender Email: yourname@gmail.com
Enter App Password:
------------------------------------
Enter Receiver Emails (comma separated): yourname@gmail.com
Enter Subject: Test from Auto Email Sender

Write your message (type END on a new line when done):
> Hello! This is a test message.
> END
Attachment Path (leave blank if none):
------------------------------------
📤 Sending email...
------------------------------------
✅ Email Sent Successfully!
📬 To: yourname@gmail.com
📝 Subject: Test from Auto Email Sender
------------------------------------
📄 Email saved in history.txt

Send another email? (yes/no): yes
------------------------------------
Enter Receiver Emails (comma separated): yourname@gmail.com
Enter Subject: Test with missing attachment

Write your message (type END on a new line when done):
> Attachment test.
> END
Attachment Path (leave blank if none): missing.pdf
------------------------------------
❌ File not found! Sending without attachment.
📤 Sending email...
------------------------------------
✅ Email Sent Successfully!
📬 To: yourname@gmail.com
📝 Subject: Test with missing attachment
------------------------------------
📄 Email saved in history.txt

Send another email? (yes/no): no

👋 Thank you for using Auto Email Sender Pro!
```


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Features ==================== -->

<a id="features"></a>

![3 Features](https://img.shields.io/badge/3-Features-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Feature | What it does |
|:--|:--|
| 📩 **Multiple Recipients** | Sends one email to many people at once, separated by commas |
| 📝 **Multi-line Messages** | Write full paragraphs and type `END` on its own line to finish |
| 📎 **File Attachments** | Attaches a file from a path you give, or sends without one if you leave it blank |
| 🛡️ **Safe Attachment Handling** | If the path is missing, invalid or a folder, it shows a warning and still sends the email |
| ✅ **Recipient Cleanup** | Extra, trailing or blank commas are removed automatically |
| 🔁 **Several Emails per Run** | After each email, choose to send another or exit without restarting |
| 📜 **Email History** | Every sent email is logged to `history.txt` with date, recipients, subject and message |
| 🔒 **Secure Login** | Uses a Gmail App Password, and the input is hidden while you type it |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Tech Stack ==================== -->

<a id="tech-stack"></a>

![4 Tech Stack](https://img.shields.io/badge/4-Tech%20Stack-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Layer | Technology | Used for |
|:------|:-----------|:---------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white) | Core logic and the command-line prompts |
| **Protocol** | ![SMTP](https://img.shields.io/badge/Gmail-SMTP-D14836?style=flat-square&logo=gmail&logoColor=white) | Sending the email through `smtp.gmail.com` |
| **Library** | ![Standard Library](https://img.shields.io/badge/Standard%20Library-4B8BBE?style=flat-square) | `smtplib`, `email.mime`, `getpass`, `os`, `datetime` |
| **Storage** | ![Text File](https://img.shields.io/badge/Storage-history.txt-2B2B2B?style=flat-square) | Logging every sent email |
| **Concepts** | SMTP and network requests · File handling · Exception handling · Loops · Functions | Practised throughout the program |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Installation ==================== -->

<a id="installation"></a>

![5 Installation](https://img.shields.io/badge/5-Installation-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

**Requirements:** Python 3.x and a Gmail account with an App Password. No libraries to install.

</div>

```bash
# 1. Clone the repository
git clone https://github.com/Charan-Code600/Auto-Email-Sender.git

# 2. Open the project folder
cd Auto-Email-Sender

# 3. Run the program
python auto_email_sender.py
```

<div align="center">

If `python` is not recognised on your system, use `python3 auto_email_sender.py` instead.

</div>

### Gmail setup (needed once, before the first run)

1. Open your Google Account and go to **Security**.
2. Turn on **2-Step Verification** if it is not already on.
3. Search for **App Passwords** and create a new one. Any name works, for example "Python Script".
4. Copy the 16-character password Google shows. Use this in the program, **not** your normal Gmail password.

> **Security note:** Never write your App Password inside the script or share it publicly. If it is ever exposed, revoke it from your Google Account and create a new one.


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>



<!-- ==================== How to Use ==================== -->

<a id="how-to-use"></a>

![6 How to Use](https://img.shields.io/badge/6-How%20to%20Use-FFB800?style=for-the-badge&labelColor=1a1a2e)

<div align="center">

| Step | What to do |
|:----:|:-----------|
| 1 | Run the script and enter your Gmail address and App Password |
| 2 | Enter one or more receiver emails, separated by commas |
| 3 | Enter a subject |
| 4 | Write your message on as many lines as you like, then type `END` on its own line |
| 5 | Enter a file path to attach, or leave it blank to send without one |
| 6 | The email is sent and a record is saved to `history.txt` |
| 7 | Type `yes` to send another email, or `no` to exit |

</div>


<!-- ==================== GLOWING DIVIDER ==================== -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12&height=4&width=1200" width="100%" />
</p>


<!-- ==================== Project Structure ==================== -->

<a id="project-structure"></a>

![7 Project Structure](https://img.shields.io/badge/7-Project%20Structure-FFB800?style=for-the-badge&labelColor=1a1a2e)

```text
Auto-Email-Sender/
├── auto_email_sender.py   # Main program
└── history.txt            # Auto-generated, log of every sent email
```


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



