import requests

TELEGRAM_TOKEN ='7781464236:AAERtY_Q1y8-dP1NDp282L4iOYV3X_uqjAI'
TELEGRAM_CHAT_ID = '8177828764'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("⚠️ Failed to send Telegram message:", e)