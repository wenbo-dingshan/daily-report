from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.scroll import scroll_to_element


def long_short_ratio_handler(spider, driver):
    try:
        buttons = [
            {"id": ":r6:", "name": "./screenshots/BTC-多空比图表.png", "option_id": ":rs:", "path": '//*[@id="__next"]/div/div[2]/div[2]/div/div[2]'},
            # //*[@id="__next"]/div/div[2]/div[2]/div/div[2]
            {"id": ":r8:", "name": "./screenshots/Binance-BTCUSDT-人数多空比.png", "option_id": ":r11:", "path": '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[3]'}
            # //*[@id="__next"]/div[2]/div[2]/div[2]/div/div[3]
        ]

        for button in buttons:
            print(f"尝试点击 {button['name']}...")

            button_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//button[@aria-controls="{button["id"]}"]'))
            )
            button_element.click()
            print(f"已点击 {button['name']}。")

            print(f"尝试选择 {button['name']} 菜单中的'1小时'选项...")
            one_hour_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, button["option_id"]))
            )
            one_hour_option.click()
            print(f"已选择 {button['name']} 菜单中的'1小时'选项。")

            scroll_to_element(driver, button_element)
            take_screenshot(driver, button['name'], button['path'])
            print(f"已截图并保存为 {button['name']}。")

    except Exception as e:
        print(f"资金流 操作失败，原因：{e}")



