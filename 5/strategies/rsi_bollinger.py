import pandas as pd

def apply_strategy(df):
    df['rsi'] = 100 - (100 / (1 + df['close'].pct_change().rolling(14).mean()))
    df['ma20'] = df['close'].rolling(20).mean()
    df['stddev'] = df['close'].rolling(20).std()
    df['upper'] = df['ma20'] + 2 * df['stddev']
    df['lower'] = df['ma20'] - 2 * df['stddev']

    latest = df.iloc[-1]
    if latest['close'] < latest['lower'] and latest['rsi'] < 30:
        return "BUY"
    elif latest['close'] > latest['upper'] and latest['rsi'] > 70:
        return "SELL"
    else:
        return None
