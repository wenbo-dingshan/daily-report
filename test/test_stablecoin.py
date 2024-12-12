from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.get_data import update_stablecoin_data

# Selenium WebDriver 设置
options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # 可选：启用无头模式
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    url = "https://defillama.com/stablecoins"
    driver.get(url)

    coin_value_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/p[1]/span[2]'))
    )
    element_text = coin_value_element.text
    print("Extracted Text:", element_text)

    today_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "value": element_text
    }
    update_stablecoin_data(today_data)

except Exception as e:
    print(f"异常: {e}")

finally:
    driver.quit()

# 加载并打印最新数据
latest_data = load_stablecoin_data()
print("Latest Data:", latest_data)