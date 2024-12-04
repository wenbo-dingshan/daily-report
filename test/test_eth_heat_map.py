import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import WebDriverOrWebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element, scroll_to_center

# 初始化 Selenium 驱动
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


try:
    # 打开目标网页
    url = "https://www.coinglass.com/zh/pro/futures/LiquidationHeatMap"
    driver.get(url)

    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:"]'))
        )

        search_box.click()
        search_box.clear()
        search_box.send_keys("ETH")

        time.sleep(2)

        dropdown_option_xpath = '//*[@id=":r5:-option-0"]'
        dropdown_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, dropdown_option_xpath))
        )

        dropdown_option.click()
        take_screenshot(driver, "./screenshots/a.png", '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[3]/div[5]')

    except Exception as e:
        print(f"ETH/USDT 热力图截图失败: {e}")

finally:
    driver.quit()
