from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element
import time


def interest_rate_handler(spider, driver):
    try:
        # 尝试点击 Cookie 按钮，若发生异常重试一次
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            print("已点击 Cookie 按钮。")
        except Exception as e:
            print("未找到或未点击 Cookie 按钮。", e)
            # 重试一次
            try:
                cookie_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                )
                cookie_button.click()
                print("已重试并点击 Cookie 按钮。")
            except Exception as e:
                print("重试失败，依然无法点击 Cookie 按钮。", e)

        # 尝试点击关闭按钮，若发生异常重试一次
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/section/span'))
            )
            close_button.click()
            print("已点击关闭按钮。")
        except Exception as e:
            print("未找到或未点击关闭按钮。", e)
            # 重试一次
            try:
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/section/span'))
                )
                close_button.click()
                print("已重试并点击关闭按钮。")
            except Exception as e:
                print("重试失败，依然无法点击关闭按钮。", e)

        # 尝试切换到 iframe，若发生异常重试一次
        try:
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[contains(@id, "cmeIframe")]'))
            )
            driver.switch_to.frame(iframe)
            print("已切换到 iframe。")
        except Exception as e:
            print("未找到或切换到 iframe 失败。", e)
            # 重试一次
            try:
                iframe = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//iframe[contains(@id, "cmeIframe")]'))
                )
                driver.switch_to.frame(iframe)
                print("已重试并切换到 iframe。")
            except Exception as e:
                print("重试失败，依然无法切换到 iframe。", e)

        # 尝试找到目标元素并截图，若发生异常重试一次
        try:
            target_element_xpath = spider.element
            target_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, target_element_xpath))
            )
            print("已找到目标元素。")

            scroll_to_element(driver, target_element)
            time.sleep(2)
            take_screenshot(driver, spider.screenshot_path, target_element_xpath)
            print("截图完成。")
        except Exception as e:
            print(f"未找到目标元素或截图失败: {e}")
            # 重试一次
            try:
                target_element_xpath = spider.element
                target_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, target_element_xpath))
                )
                print("已重试并找到目标元素。")

                scroll_to_element(driver, target_element)
                time.sleep(2)
                take_screenshot(driver, spider.screenshot_path, target_element_xpath)
                print("截图完成。")
            except Exception as e:
                print(f"重试失败，依然无法找到目标元素或截图失败: {e}")

    except Exception as e:
        print(f"美联储利率截图失败: {e}")