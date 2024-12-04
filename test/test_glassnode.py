import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.parser import get_login_credentials
from utils.screenshot import take_screenshot

options = Options()
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


try:
    username, password = get_login_credentials("../config/config.ini")
    url = "https://studio.glassnode.com/workbench/506f9756-e470-4781-5ed1-1a8391d5f308?s=1704038400&u=1730191780&zoom=ytd"
    driver.get(url)

    try:
        time.sleep(2)

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/button'))
        )
        login_button.click()

        username_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        username_box.send_keys(username)
        password_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="current-password"]'))
        )
        password_box.send_keys(password)

        submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="base"]/div[1]/div/div/div/div[7]/button'))
        )
        submit_button.click()

        time.sleep(2)

        take_screenshot(driver, '../screenshots/BTC 虾净值持仓.png','//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div')


    except Exception as e:
        print(f"截图失败: {e}")

finally:
    driver.quit()
