from utils.chart_capture import select_chart_area, capture_chart_region
from utils.indicators import analyze_chart
from utils.telegram import send_signal
from config import SYMBOL as symbol
import time
import webbrowser

# Step 1: Launch trading page
webbrowser.open("https://pocketoption.com/en/cabinet/")
time.sleep(5)

# Step 2: Initialize
print("🔧 Initializing components...")

# Step 3: Chart area selection (mouse drag)
chart_area = select_chart_area()
if not chart_area:
    print("❌ Chart area selection failed. Exiting.")
    exit()

print("✅ Chart area selected.")

# Step 4: Start signal loop
print("📡 Starting live signal engine (every 30 seconds)...")

while True:
    img = capture_chart_region(chart_area)
    img.save("debug_chart.png") 
    
    if img is None:
        print("❌ Failed to capture chart image.")
        continue

    signal = analyze_chart(img)
    if signal:
        print(f"📢 SIGNAL for {symbol}: {signal}")
        send_signal(f"📢 SIGNAL for {symbol}: {signal}")
    else:
        print("⏳ No trade condition met.")
    
    time.sleep(30)

