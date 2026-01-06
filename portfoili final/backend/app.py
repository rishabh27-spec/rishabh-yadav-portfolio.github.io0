from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Python backend is running! 🚀"

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not (name and email and message):
        return jsonify({"success": False, "msg": "All fields required"}), 400

    try:
        # Set up the email message
        msg = EmailMessage()
        msg["From"] = os.getenv("EMAIL")
        msg["To"] = os.getenv("EMAIL")
        msg["Subject"] = f"Portfolio Contact - {name}"
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # SMTP server setup (using Gmail for example)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
            server.send_message(msg)

        return jsonify({"success": True, "msg": "Message sent successfully"})

    except Exception as e:
        return jsonify({"success": False, "msg": "Server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
