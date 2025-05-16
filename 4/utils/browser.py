import undetected_chromedriver as uc

def launch_browser():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options)
    driver.get("https://pocketoption.com/en/cabinet/demo-otc/")
    print("🟢 Please log in and load the chart.")
    input("🔐 Press ENTER after login and chart is visible...")
    return driver

def extract_candles(driver):
    script = """
    let bars = window.tvWidget?.chart()?.getVisibleSeries()[0]?.series()._bars || [];
    return bars.map(bar => {
        return {
            time: bar.time / 1000,
            open: bar.value[0],
            high: bar.value[1],
            low: bar.value[2],
            close: bar.value[3]
        };
    });
    """
    try:
        return driver.execute_script("return " + script)
    except Exception as e:
        print("⚠️ Error extracting candles:", e)
        return []