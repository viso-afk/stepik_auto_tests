from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # находим картинку-сундук и берём x из атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    # считаем значение
    y = calc(x)

    # вводим ответ
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # выбираем radiobutton
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()