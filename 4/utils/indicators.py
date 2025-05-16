import pandas as pd
from ta.trend import EMAIndicator, MACD, ADXIndicator
from ta.momentum import RSIIndicator
from utils.telegram import send_telegram_message

def analyze_and_signal(candles):
    df = pd.DataFrame(candles)
    if len(df) < 20:
        return

    df['ema'] = EMAIndicator(df['close'], window=10).ema_indicator()
    df['rsi'] = RSIIndicator(df['close'], window=14).rsi()
    macd = MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    adx = ADXIndicator(df['high'], df['low'], df['close'])
    df['adx'] = adx.adx()

    last = df.iloc[-1]
    if last['close'] > last['ema'] and last['macd'] > last['macd_signal'] and last['rsi'] > 50 and last['adx'] > 25:
        signal = "BUY"
    elif last['close'] < last['ema'] and last['macd'] < last['macd_signal'] and last['rsi'] < 50 and last['adx'] > 25:
        signal = "SELL"
    else:
        signal = None

    if signal:
        msg = f"📢 SIGNAL: {signal}\nPrice: {last['close']}\nTime: {last['time']}"
        print(msg)
        send_telegram_message(msg)
    else:
        print("⏳ No strong signal detected.")