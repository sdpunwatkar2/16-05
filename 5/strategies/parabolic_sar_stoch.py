import pandas as pd
import ta

def apply_strategy(df):
    df = df.copy()

    # Indicators
    df['sar'] = ta.trend.psar(df['high'], df['low'], df['close'])
    stoch = ta.momentum.StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)
    df['stoch_k'] = stoch.stoch()
    df['stoch_d'] = stoch.stoch_signal()

    latest = df.iloc[-1]

    # Buy condition
    if latest['close'] > latest['sar'] and latest['stoch_k'] < 30 and latest['stoch_k'] > latest['stoch_d']:
        return "BUY"

    # Sell condition
    if latest['close'] < latest['sar'] and latest['stoch_k'] > 70 and latest['stoch_k'] < latest['stoch_d']:
        return "SELL"

    return None
