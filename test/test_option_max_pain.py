from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # 打开目标网页
    url = "https://www.coinglass.com/zh/pro/options/max-pain"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]'))
    )

    take_screenshot(driver, "btc_option_max_pain.png", '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')


    eth_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=":R59l6jilaqm:"]'))
    )

    eth_button.click()
    eth_table_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]'))
    )

    take_screenshot(driver, "eth_option_max_pain.png", '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')

except Exception as e:
    print(f"异常: {e}")

finally:
    driver.quit()
