from utils.browser import launch_browser, extract_candles
from utils.indicators import analyze_and_signal
from utils.telegram import send_telegram_message
import time

print("🔧 Initializing components...")
driver = launch_browser()
print("✅ Browser launched")
send_telegram_message("🚀 OTC Trading Bot Started. Monitoring...")
print("✅ Telegram ready")

while True:
    candles = extract_candles(driver)
    if candles:
        analyze_and_signal(candles)
    time.sleep(15)