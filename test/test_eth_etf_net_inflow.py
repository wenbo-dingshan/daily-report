from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element
import time

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # 打开目标网页
    url = "https://www.coinglass.com/zh/eth-etf"
    driver.get(url)

    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=":R5aj6klaeqm:"]'))
        )
        search_box.click()
        time.sleep(2)


        scroll_to_element(driver, search_box)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]'))
        )

        take_screenshot(driver, "./screenshots/a.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]') #//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[4]/div[2]

    except Exception as e:
        print(f"主路径元素加载失败，尝试备用路径: {e}")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[4]/div[2]'))
            )

            scroll_to_element(driver, element)

            take_screenshot(driver, "./screenshots/b.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div/div[4]/div[2]')
        except Exception as e2:
            print(f"备用路径也加载失败: {e2}")

finally:
    driver.quit()
