from pynput import mouse
import pyautogui

def select_chart_area():
    print("🖱️ Please select the chart area (drag mouse)...")
    coords = []

    def on_click(x, y, button, pressed):
        if pressed:
            coords.clear()
            coords.append((x, y))
        else:
            coords.append((x, y))
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    if len(coords) == 2:
        (x1, y1), (x2, y2) = coords
        left = min(x1, x2)
        top = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return (left, top, width, height)
    else:
        return None

def capture_chart_region(region):
    return pyautogui.screenshot(region=region)
