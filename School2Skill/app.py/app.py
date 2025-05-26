from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    receiver_email = "nmarnien@gmail.com"

    msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
    msg['Subject'] = "New Submission on School2Skill"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
    except Exception as e:
        print("Failed to send email:", e)

    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
