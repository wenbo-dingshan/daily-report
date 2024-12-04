from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element, scroll_to_center

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # 打开目标网页
    url = "https://www.coinglass.com/zh/options"
    driver.get(url)

    scroll_to_center(driver)

    btc_table_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[6]/div'))
    )

    take_screenshot(driver, "BTC_option.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[6]/div')


    eth_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=":r9:"]'))
    )

    eth_button.click()
    eth_table_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[6]/div'))
    )

    take_screenshot(driver, "ETH_option.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[6]/div')

    take_screenshot(driver, "option_volume.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[7]/div/div')

except Exception as e:
    print(f"异常: {e}")

finally:
    driver.quit()
