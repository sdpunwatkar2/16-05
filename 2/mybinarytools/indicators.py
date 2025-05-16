import pandas as pd
import ta

def calculate_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd_diff()
    bb = ta.volatility.BollingerBands(df['close'])
    df['bb_low'] = bb.bollinger_lband()
    df['bb_high'] = bb.bollinger_hband()
    return df

def is_buy_signal(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    return (
        latest['rsi'] < 30 and
        latest['macd'] > 0 and
        latest['close'] < latest['bb_low'] and
        latest['close'] > latest['open'] and
        previous['close'] < previous['open']
    )

def is_sell_signal(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    return (
        latest['rsi'] > 70 and
        latest['macd'] < 0 and
        latest['close'] > latest['bb_high'] and
        latest['close'] < latest['open'] and
        previous['close'] > previous['open']
    )