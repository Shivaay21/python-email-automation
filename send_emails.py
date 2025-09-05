import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

# Gmail SMTP settings
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load environment variables
current_dir = Path(__file__).resolve().parent
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Coding is Fun Corp.", sender_email))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email  # Send yourself a copy

    # Plain text version
    msg.set_content(
        f"""\
Hi {name},

I hope you are well.

This is a reminder that {amount} Rs for invoice {invoice_no} is due on {due_date}.

I would be grateful if you could confirm that the payment is on track.

Best regards,
Your Name
"""
    )

    # HTML version
    msg.add_alternative(
        f"""\
<html>
    <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>This is a reminder that <strong>{amount} Rs</strong> for invoice <strong>{invoice_no}</strong> is due on <strong>{due_date}</strong>.</p>
        <p>Please confirm that payment is on track.</p>
        <p>Best regards,<br>Your Name</p>
    </body>
</html>
""",
        subtype="html",
    )

    # Send the email
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.send_message(msg)
        print(f"✅ Email sent to {receiver_email}")

# Optional test send
if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Shivam Sharma",
        receiver_email="shivaayshc19@gmail.com",
        due_date="11, Aug 2025",
        invoice_no="INV-21-12-009",
        amount="500"
    )
