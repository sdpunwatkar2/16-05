import pandas as pd

def apply_strategy(df):
    df['ema_fast'] = df['close'].ewm(span=5, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=20, adjust=False).mean()
    df['macd'] = df['ema_fast'] - df['ema_slow']
    df['signal_line'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['adx'] = df['high'] - df['low']
    df['adx'] = df['adx'].rolling(window=14).mean()

    latest = df.iloc[-1]
    if latest['ema_fast'] > latest['ema_slow'] and latest['macd'] > latest['signal_line'] and latest['adx'] > 20:
        return "BUY"
    elif latest['ema_fast'] < latest['ema_slow'] and latest['macd'] < latest['signal_line'] and latest['adx'] > 20:
        return "SELL"
    else:
        return None
