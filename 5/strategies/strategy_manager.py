from strategies.ema_macd_rsi import apply_strategy as ema_macd_rsi
from strategies.bollinger_adx import apply_strategy as bollinger_adx
from strategies.parabolic_sar_stoch import apply_strategy as parabolic_sar_stoch

def evaluate_strategies(df):
    votes = {"BUY": 0, "SELL": 0}

    for strat in [ema_macd_rsi, bollinger_adx, parabolic_sar_stoch]:
        decision = strat(df)
        if decision:
            votes[decision] += 1

    if votes["BUY"] >= 2:
        return "BUY"
    elif votes["SELL"] >= 2:
        return "SELL"
    else:
        return None
