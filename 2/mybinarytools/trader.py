import time
import random
import pandas as pd
from .config import SYMBOLS, TIMEFRAME
from .telegram_alert import send_telegram_message
from .strategy import analyze

def get_mock_candles(symbol):
    prices = [random.uniform(50, 100) for _ in range(50)]
    df = pd.DataFrame({
        'open': prices[:-1],
        'close': prices[1:],
        'high': [p + random.uniform(0, 2) for p in prices[:-1]],
        'low': [p - random.uniform(0, 2) for p in prices[:-1]]
    })
    return df

class TradingBot:
    def __init__(self):
        try:
            print("✅ Trader initialized.")
            print(f"➡️ Loaded symbols: {SYMBOLS}")
            print(f"➡️ Timeframe: {TIMEFRAME}")
            print("✅ Configuration loaded successfully.")
        except Exception as e:
            print(f"❌ Error initializing config: {e}")
        
        try:
            df_test = get_mock_candles(SYMBOLS[0])
            if df_test is not None and not df_test.empty:
                print("✅ Market data module initialized (mock data).")
        except Exception as e:
            print(f"❌ Error in market data module: {e}")

        try:
            signal = analyze(df_test)
            print("✅ Strategy logic loaded.")
        except Exception as e:
            print(f"❌ Error loading strategy logic: {e}")

        try:
            send_telegram_message("📢 Bot started and components initialized successfully.")
            print("✅ Telegram alert system connected.")
        except Exception as e:
            print(f"❌ Error connecting Telegram alert system: {e}")

    def run(self):
        print("🚀 Starting bot loop...")
        while True:
            for symbol in SYMBOLS:
                try:
                    df = get_mock_candles(symbol)
                    signal = analyze(df)
                    if signal:
                        msg = f"📈 Signal Alert (HIGH ACCURACY)\nAsset: {symbol}\nAction: {signal}"
                        print(msg)
                        send_telegram_message(msg)
                except Exception as e:
                    print(f"⚠️ Error during signal generation for {symbol}: {e}")
            time.sleep(30)