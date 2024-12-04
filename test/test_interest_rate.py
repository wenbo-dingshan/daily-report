from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.scroll import scroll_to_element
from utils.screenshot import take_screenshot
import time

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # 打开目标网页
    url = "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
    driver.get(url)
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_button.click()
        print("已点击 Cookie 按钮。")
    except Exception as e:
        print("未找到或未点击 Cookie 按钮。", e)

    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/section/span'))
        )
        close_button.click()
        print("已点击关闭按钮。")
    except Exception as e:
        print("未找到或未点击关闭按钮。", e)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[contains(@id, "cmeIframe")]'))
    )
    driver.switch_to.frame(iframe)
    print("已切换到 iframe。")

    target_element_xpath = '//*[@id="MainContent_pnlContainer"]/div[3]/div/div'
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, target_element_xpath))
    )
    print("已找到目标元素。")

    scroll_to_element(driver, target_element)
    time.sleep(2)
    take_screenshot(driver, "test_降息.png", target_element_xpath)

except Exception as e:
    print(f"美联储利率截图失败: {e}")

finally:
    driver.quit()
