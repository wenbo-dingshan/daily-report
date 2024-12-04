from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
import time


def eth_heat_map_handler(spider, driver):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:"]'))
        )

        search_box.click()
        search_box.send_keys("ETH")

        time.sleep(4)

        dropdown_option_xpath = '//*[@id=":r5:-option-0"]'
        dropdown_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, dropdown_option_xpath))
        )

        dropdown_option.click()
        take_screenshot(driver, spider.screenshot_path, spider.element)

    except Exception as e:
        print(f"ETH/USDT 热力图截图失败: {e}")