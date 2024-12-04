import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from utils.scroll import scroll_to_element
from utils.download import save_to_file


def macro_event_handler(spider, driver):
    try:
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "buttonLine")))

        time_frame_button = button.find_element(By.ID, "timeFrame_thisWeek")
        time_frame_button.click()

        filter_state_button = button.find_element(By.ID, "filterStateButton")
        country_options = driver.find_element(By.CLASS_NAME, "countryOption")
        country_checkboxes = country_options.find_elements(By.CSS_SELECTOR, "[checked=checked]")

        filter_state_button.click()

        importance_2_button = button.find_element(By.ID, "importance2")
        scroll_to_element(driver, importance_2_button)
        # importance_2_button.click()
        # print("已点击重要性2")

        importance_3_button = button.find_element(By.ID, "importance3")
        scroll_to_element(driver, importance_3_button)
        importance_3_button.click()
        print("已点击重要性3")

        for checkbox in country_checkboxes:
            if checkbox.get_attribute("value") != "5":
                scroll_to_element(driver, checkbox)
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f"[value='{checkbox.get_attribute('value')}']")))
                if checkbox.get_attribute("value") != "5" and checkbox.is_selected():
                    checkbox.click()

        submit_button = button.find_element(By.ID, "ecSubmitButton")
        scroll_to_element(driver, submit_button)
        wait.until(element_to_be_clickable((By.ID, "ecSubmitButton")))
        submit_button.click()
        print("已点击应用")

        table_data = wait.until(
            EC.visibility_of_element_located((By.ID, "economicCalendarData"))
        )
        print("表格数据已加载")
        print(table_data.text)

        save_to_file(spider.output_path, table_data.text)


    except (TimeoutException, ElementNotInteractableException) as e:
        print("表格未加载，尝试重新点击")
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "buttonLine")))
        filter_state_button = button.find_element(By.ID, "filterStateButton")
        scroll_to_element(driver, filter_state_button)
        filter_state_button.click()
        print("已重新点击过滤按钮")

        submit_button = button.find_element(By.ID, "ecSubmitButton")
        wait.until(element_to_be_clickable((By.ID, "ecSubmitButton")))
        submit_button.click()
        print("再次点击应用完成")
        table_data = wait.until(
            EC.visibility_of_element_located((By.ID, "economicCalendarData"))
        )
        print(table_data.text)
        save_to_file(spider.output_path, table_data.text)

    except Exception as e:
        print(f"处理宏观事件数据失败: {e}")