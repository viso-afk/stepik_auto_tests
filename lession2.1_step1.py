from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    # считываем x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # вычисляем значение
    y = calc(x)

    # вводим ответ
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

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