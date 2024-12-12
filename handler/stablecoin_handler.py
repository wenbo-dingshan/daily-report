from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.get_data import update_stablecoin_data
from datetime import datetime


def stablecoin_handler(spider, driver):
    try:
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
        take_screenshot(driver, spider.screenshot_path, spider.element)

    except Exception as e:
        print(f": {e}")
