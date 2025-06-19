📬 Flask Form App
This is a Flask web app that collects user details through a form and stores them in a SQLite database. After submission, it sends a confirmation email to the user.

✅ What it does
Collects user data: name, email, date, occupation

Stores it in a local database

Sends a thank-you email using SMTP (Gmail)

Shows submission success or failure messages

💡 Technologies Used
Python 🐍

Flask 🌐

SQLite 💾

Flask-Mail ✉️

▶️ How to Run
bash

pip install flask flask_sqlalchemy flask_mail
python app.py
