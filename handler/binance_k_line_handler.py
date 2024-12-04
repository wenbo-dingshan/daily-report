import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot


def binance_k_line_handler(spider, driver):
    try:
        url = "https://www.coinglass.com/tv/zh/Binance_BTCUSDT"
        driver.get(url)

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//iframe[@title="Financial Chart"]'))
        )
        driver.switch_to.frame(iframe)

        time.sleep(2)

        table_xpath = '/html/body/div[2]/div[3]/div/div[1]/div[2]/table'
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, table_xpath))
        )
        take_screenshot(driver, "./screenshots/Binance-1小时K线.png", table_xpath)
        print("1小时 K 线表格截图完成")

        driver.switch_to.default_content()

        day_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div/button[7]'))
        )
        day_button.click()
        print("已点击 1天 按钮，等待表格更新")

        driver.switch_to.frame(iframe)  # 再次切换到 iframe
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, table_xpath))
        )

        take_screenshot(driver, "./screenshots/Binance-1天K线.png", table_xpath)
        print("1天 K 线表格截图完成")

    except Exception as e:
        print(f"BTC K 线图表截图失败: {e}")
