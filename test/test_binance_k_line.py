from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_center

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    url = "https://www.coinglass.com/tv/zh/Binance_BTCUSDT"
    driver.get(url)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@title="Financial Chart"]'))
    )
    driver.switch_to.frame(iframe)

    table_xpath = '/html/body/div[2]/div[3]/div/div[1]/div[2]/table'
    table_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, table_xpath))
    )
    take_screenshot(driver, "test_binance_1hr_k_line.png", table_xpath)
    print("1小时 K 线表格截图完成")

    driver.switch_to.default_content()

    day_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div/button[7]'))
    )
    day_button.click()
    print("已点击 1天 按钮，等待表格更新")

    driver.switch_to.frame(iframe)  # 再次切换到 iframe
    updated_table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, table_xpath))
    )

    take_screenshot(driver, "test_binance_day_k_line.png", table_xpath)
    print("1天 K 线表格截图完成")


except Exception as e:
    print(f"异常: {e}")

finally:
    driver.quit()
