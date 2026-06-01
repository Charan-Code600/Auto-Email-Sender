


# 📧 Auto Email Sender Pro

A professional Python automation project that allows users to send emails through Gmail SMTP with support for multiple recipients, file attachments, email history tracking, and secure authentication using Gmail App Passwords.

---

## 🌟 Key Features

* 📩 Send emails using Gmail SMTP
* 👥 Send emails to multiple recipients at once
* 📎 Attach files (PDF, Images, Documents, etc.)
* 📝 Custom subject and message support
* 📜 Automatically save email history
* 🔒 Secure Gmail App Password authentication
* ⚠️ Built-in error handling

---

## 🛠️ Technologies Used

* Python
* smtplib
* email.mime
* datetime
* os

---

## 📂 Project Structure

```text
Auto-Email-Sender-Pro/
│
├── main.py
├── history.txt
├── README.md
└── attachments/
```

---

## 🚀 How It Works

1. User enters Gmail address
2. User enters Gmail App Password
3. User enters recipient email(s)
4. User enters subject and message
5. User optionally attaches a file
6. Email is sent successfully
7. Email details are stored in history.txt

---

## 🔐 Gmail Setup

This project requires a Gmail App Password.

Steps:

1. Enable 2-Step Verification in your Google Account
2. Open Google App Passwords
3. Generate a new App Password
4. Use the generated password inside the program

⚠️ Do not use your normal Gmail password.

---

## ▶️ Installation & Usage

Clone the repository:

```bash
git clone https://github.com/your-username/Auto-Email-Sender-Pro.git
```

Move into the project folder:

```bash
cd Auto-Email-Sender-Pro
```

Run the program:

```bash
python main.py
```

---

## 📄 Example

```text
Enter Sender Email:
example@gmail.com

Enter App Password:
****************

Enter Receiver Emails:
user1@gmail.com,user2@gmail.com

Enter Subject:
Project Update

Write your message:
Hello Team

Attachment Path:
report.pdf

✅ Email Sent Successfully!
📄 Email saved in history.txt
```

---

## 📜 Email History

Every successful email is automatically recorded in:

```text
history.txt
```

Saved Information:

* Date & Time
* Recipient(s)
* Subject
* Message

---

## 🎯 Future Enhancements

* HTML Email Support
* Bulk Email Sending from CSV
* Email Templates
* GUI Version (Tkinter)
* Scheduled Email Sending
* Email Analytics Dashboard

---

## 💡 Learning Outcomes

Through this project, I learned:

* SMTP Email Automation
* Gmail App Password Authentication
* Working with MIME Messages
* File Attachments in Emails
* Error Handling
* Python Automation Techniques

---

## 👨‍💻 Author

**Charan**

Python Automation Project built for learning and portfolio development.

