import pandas as pd
import ta

def apply_strategy(df):
    df = df.copy()

    # Indicators
    bb = ta.volatility.BollingerBands(df['close'], window=20, window_dev=2)
    df['bb_upper'] = bb.bollinger_hband()
    df['bb_lower'] = bb.bollinger_lband()
    df['adx'] = ta.trend.adx(df['high'], df['low'], df['close'])

    latest = df.iloc[-1]

    # Buy condition
    if latest['close'] < latest['bb_lower'] and latest['adx'] > 25:
        return "BUY"

    # Sell condition
    if latest['close'] > latest['bb_upper'] and latest['adx'] > 25:
        return "SELL"

    return None
