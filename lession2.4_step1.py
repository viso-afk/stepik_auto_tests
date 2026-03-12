from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ждём, пока цена станет $100 (не меньше 12 секунд)
    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # бронируем
    browser.find_element(By.ID, "book").click()

    # решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(30)
    browser.quit()