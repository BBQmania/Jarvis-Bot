import os
import requests
from flask import Flask, request

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    message = data.get('message', '🚨 Alert bez treści')
    send_telegram_message(message)
    return {'status': 'ok'}

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
