from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("window.scrollBy(0, -100);")
    print("已滚动到目标元素")

def scroll_to_center(driver, element=None):
    if element:
        driver.execute_script("""
            const element = arguments[0];
            const elementRect = element.getBoundingClientRect();
            const absoluteElementTop = elementRect.top + window.pageYOffset;
            const middle = absoluteElementTop - (window.innerHeight / 2);
            window.scrollTo({ top: middle, behavior: 'smooth' });
        """, element)
    else:
        driver.execute_script("""
            const middle = document.body.scrollHeight / 2 - window.innerHeight / 2;
            window.scrollTo({ top: middle, behavior: 'smooth' });
        """)