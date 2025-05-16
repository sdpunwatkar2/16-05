from .indicators import calculate_indicators, is_buy_signal, is_sell_signal

def analyze(df):
    df = calculate_indicators(df)
    if is_buy_signal(df):
        return "BUY"
    elif is_sell_signal(df):
        return "SELL"
    return None