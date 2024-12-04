import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.parser import get_login_credentials
from utils.screenshot import take_screenshot


def glassnode_handler(spider, driver):
    try:
        username, password = get_login_credentials()
        driver.get(spider.url)

        time.sleep(20)

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/button'))
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

        time.sleep(20)

        take_screenshot(driver, spider.screenshot_path, spider.element)

    except Exception as e:
        print(f"GlassNode {spider.name} 失败: {e}，正在重新截图 {spider.name}")
        time.sleep(20)
        take_screenshot(driver, spider.screenshot_path, spider.element)
