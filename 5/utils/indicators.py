import cv2
import numpy as np
from PIL import Image

def analyze_chart(image):
    if image is None:
        print("❌ Image capture failed: received None")
        return None

    img_array = np.array(image)
    if img_array.size == 0:
        print("❌ Captured image is empty.")
        return None

    try:
        # Convert image to OpenCV format
        img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # 1. Brightness Analysis
        brightness = np.mean(gray)

        # 2. Edge Density Analysis (volatility)
        edges = cv2.Canny(gray, threshold1=50, threshold2=150)
        edge_density = np.sum(edges) / (gray.shape[0] * gray.shape[1])

        # 3. Red vs Green Candle Dominance
        red_pixels = np.sum((img[:, :, 0] > 150) & (img[:, :, 1] < 100))
        green_pixels = np.sum((img[:, :, 1] > 150) & (img[:, :, 0] < 100))

        # Heuristics
        if brightness < 90 and red_pixels > green_pixels * 1.3:
            return "SELL"
        elif brightness > 150 and green_pixels > red_pixels * 1.3:
            return "BUY"
        elif edge_density > 0.05:
            return None  # avoid trading
        else:
            return None

    except cv2.error as e:
        print(f"⚠️ OpenCV Error during image processing: {e}")
        return None
