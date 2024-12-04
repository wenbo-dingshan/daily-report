from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot

def option_max_pain_handler(spider, driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, spider.element))
        )

        take_screenshot(driver, "./screenshots/BTC-期权最大痛点.png", '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')

        eth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id=":R59l6jilaqm:"]'))
        )

        eth_button.click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]'))
        )

        take_screenshot(driver, "./screenshots/ETH-期权最大痛点.png", '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]')

    except Exception as e:
        print(f"期权最大痛点图表截图失败: {e}")
