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
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    url = "https://www.coinglass.com/zh/bitcoin-etf"
    driver.get(url)

    try:
        scroll_to_center(driver)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div[7]/div[1]')) # //*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]
        )
        take_screenshot(driver, "./screenshots/a.png", '//*[@id="__next"]/div[2]/div[1]/div[2]/div[7]/div[1]') # //*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]

    except Exception as e:
        print(f"主路径元素加载失败，尝试备用路径: {e}")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]'))
            )
            take_screenshot(driver, "./screenshots/b.png", '//*[@id="__next"]/div[2]/div[2]/div[2]/div[6]/div[1]')
        except Exception as e2:
            print(f"备用路径也加载失败: {e2}")

finally:
    driver.quit()
