from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element
import time


def eth_eft_net_inflow_handler(spider, driver):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":R5aj6klaeqm:"]'))
        )
        search_box.click()
        time.sleep(2)


        scroll_to_element(driver, search_box)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, spider.element))
        )

        take_screenshot(driver, spider.screenshot_path, spider.element)

    except Exception as e:
        print(f"主路径元素加载失败，尝试备用路径: {e}")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]'))
            )

            scroll_to_element(driver, element)

            take_screenshot(driver, spider.screenshot_path, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]')
        except Exception as e2:
            print(f"备用路径也加载失败-ETH-ETF净流入(USD)截图失败: {e2}")
