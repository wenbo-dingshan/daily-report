from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot
import importlib
import re


def initialize_driver():
    options = Options()
    service = Service()
    options.add_argument("user-agent=Mozilla/5.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

class Spider:
    def __init__(self, task):
        self.url = task["url"]
        self.name = task.get("name")
        self.element = task.get("element")
        self.screenshot_path = task.get("screenshot_path") or f"./screenshots/{self.generate_default_filename()}.png"
        self.output_path = task.get("output_path") or f"./data/{self.generate_default_filename()}.txt"
        self.custom_handler = task.get("custom_handler")

    def generate_default_filename(self):
        if hasattr(self, 'name') and self.name:
            return self.name

        match = re.search(r"https?://(?:www\.)?([^/]+)", self.url)
        if match:
            domain = match.group(1)
            domain = '.'.join(domain.split('.')[-2:])
            return domain.replace(".", "_")
        return self.url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "_")

    def load_handler(self):
        if self.custom_handler:
            try:
                module = importlib.import_module(f"handler.{self.custom_handler}")
                return getattr(module, self.custom_handler)
            except (ImportError, AttributeError) as e:
                print(f"加载 handler '{self.custom_handler}' 失败: {e}")
                return None
        return None

    def run(self):
        print(f"正在爬取: {self.url}")
        driver = initialize_driver()

        try:
            driver.get(self.url)
            WebDriverWait(driver, 60).until(
                lambda d: d.current_url != self.url or "CAPTCHA" not in d.title
            )
            handler_func = self.load_handler()
            if handler_func:
                print(f"执行自定义 handler: {self.custom_handler}")
                handler_func(self, driver)
            else:
                print("执行默认截图逻辑...")
                take_screenshot(driver, self.screenshot_path, self.element)
        finally:
            driver.quit()