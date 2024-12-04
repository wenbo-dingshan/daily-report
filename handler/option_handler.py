from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_center


def option_handler(spider, driver):
    try:
        scroll_to_center(driver)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, spider.element))
        )

        take_screenshot(driver, "./screenshots/BTC-期权持仓.png", spider.element)

        eth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id=":r9:"]'))
        )

        eth_button.click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, spider.element))
        )

        take_screenshot(driver, "./screenshots/ETH-期权持仓.png", spider.element)

        take_screenshot(driver, "./screenshots/期权成交量.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[7]/div/div')

    except Exception as e:
        print(f"期权图表截图失败: {e}")
