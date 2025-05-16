# pocketbot/bot.py

import socketio
import pandas as pd
from datetime import datetime
from .config import SYMBOLS
from .indicators import apply_indicators, is_buy, is_sell
from .telegram import send_telegram_message

sio = socketio.Client()
candles = {symbol: [] for symbol in SYMBOLS}

@sio.event
def connect():
    print("✅ Connected to Pocket Option WebSocket.")
    send_telegram_message("🚀 OTC Signal Bot Connected.")

    for symbol in SYMBOLS:
        base = symbol.split("_")[0].lower()
        sio.emit("subscribeMessage", {
            "name": "candle-generated",
            "symbol": f"{base}_usd"
        })
        print(f"📡 Subscribed to {base}_usd")

@sio.event
def connect_error(data):
    print("❌ Connection failed:", data)

@sio.event
def disconnect():
    print("🔌 Disconnected from Pocket Option WebSocket.")

@sio.on("candle-generated")
def on_candle(data):
    try:
        symbol_raw = data.get("symbol", "").upper().replace("_USD", "_OTC")
        for symbol in SYMBOLS:
            if symbol.upper() == symbol_raw:
                candles[symbol].append({
                    'time': datetime.fromtimestamp(data['from']),
                    'open': data['open'],
                    'close': data['close'],
                    'high': data['max'],
                    'low': data['min']
                })
                if len(candles[symbol]) > 30:
                    df = pd.DataFrame(candles[symbol][-30:])
                    df = apply_indicators(df)
                    signal = None
                    if is_buy(df):
                        signal = "BUY"
                    elif is_sell(df):
                        signal = "SELL"
                    if signal:
                        msg = f"📢 SIGNAL ({symbol})\nDirection: {signal}\nTime: {datetime.now().strftime('%H:%M:%S')}"
                        print(msg)
                        send_telegram_message(msg)
    except Exception as e:
        print(f"⚠️ Error processing candle for {symbol}: {e}")

def run():
    print("🔄 Connecting to Pocket Option via Socket.IO...")
    sio.connect("https://api-c.po.market", transports=["websocket"])
    sio.wait()
