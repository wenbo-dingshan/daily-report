import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.scroll import scroll_to_element
import time


def take_screenshot(driver, file_path, element_xpath=None):
    print(f"保存截图至: {file_path}")
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    if element_xpath:
        try:
            print(f"等待元素加载: {element_xpath}")
            time.sleep(10)
            driver.execute_script("window.scrollBy(0, 300);")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )
            print("等待页面动态加载完成...")
            for _ in range(3):
                prev_dom = driver.execute_script("return document.body.innerHTML")
                time.sleep(2)
                curr_dom = driver.execute_script("return document.body.innerHTML")
                if prev_dom == curr_dom:
                    break
            else:
                print("警告: 页面可能仍在加载动态内容。")
                time.sleep(2)
            element = driver.find_element(By.XPATH, element_xpath)
            print(f"滚动到元素: {element_xpath}")
            scroll_to_element(driver, element)
            print(f"对指定元素进行截图: {element_xpath}")
            time.sleep(2)
            element.screenshot(file_path)
        except Exception as e:
            print(f"元素截图失败，原因: {e}. 尝试全页面截图...")
            driver.save_screenshot(file_path)
    else:
        driver.save_screenshot(file_path)