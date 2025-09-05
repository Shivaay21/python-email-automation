# python-email-automation
Lightweight Python project for automating emails with scheduling and CSV support, built using smtplib, schedule, and pandas.
Email Automation Project

📌 Overview

This project is a Python-based Email Automation Tool that helps in sending bulk or scheduled emails automatically.
It can read recipient details from a CSV file, schedule emails at a specific time, and keep credentials safe using environment variables.

🚀 Features

Send emails automatically using Python.

Bulk email sending from CSV file (name, email, subject, body).

Schedule emails at specific times.

Environment variable support for credentials security.

Simple and lightweight project (perfect for learning & resumes).

🛠️ Tech Stack

Python

smtplib & email (for sending emails)

pandas (for reading CSV files)

schedule (for scheduling emails)

python-dotenv (for hiding credentials)

📂 Project Structure
Email-Automation/
│── main.py
│── emails.csv
│── .env
│── requirements.txt
│── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/Shivaay21/python-email-automation

cd email-automation


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows


Install dependencies:

pip install -r requirements.txt


Create a .env file and add your credentials:

EMAIL=your_email@gmail.com
PASSWORD=your_app_password

▶️ Usage

Run the script:

python main.py


Emails will be sent as per the CSV file or scheduled time.

You can modify main.py to customize subject, body, or schedule.

📌 Example CSV File (emails.csv)
name,email,subject,body
Shivam,shivam@example.com,Hello Shivam,This is a test email.
Alfred,alfred@example.com,Reminder,Don’t forget the meeting tomorrow.

🎯 Future Enhancements

Add GUI using Tkinter.

Support for HTML formatted emails.

Email tracking (sent/failed logs).
