from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_center


def btc_eft_net_flow_handler(spider, driver):
    try:
        scroll_to_center(driver)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, spider.element))
        )
        take_screenshot(driver, spider.screenshot_path, spider.element)

    except Exception as e:
        print(f"主路径元素加载失败，尝试备用路径: {e}")
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div[6]/div[1]/div'))
            )
            take_screenshot(driver, spider.screenshot_path, '//*[@id="__next"]/div[2]/div[1]/div[2]/div[6]/div[1]/div')
        except Exception as e2:
            print(f"备用路径也加载失败-BTC-ETF净流出净流入(USD)截图失败: {e2}")