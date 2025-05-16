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
    def run(self):
        print("🔁 Starting bot...")
        while True:
            for symbol in SYMBOLS:
                df = get_mock_candles(symbol)
                signal = analyze(df)
                if signal:
                    msg = f"📈 Signal Alert (HIGH ACCURACY)\nAsset: {symbol}\nAction: {signal}"
                    print(msg)
                    send_telegram_message(msg)
            time.sleep(30)