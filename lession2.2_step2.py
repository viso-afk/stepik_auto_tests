from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    # читаем x и считаем ответ
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")

    # скроллим к полю ввода (а заодно и к остальным элементам)
    browser.execute_script("arguments[0].scrollIntoView(true);", answer)

    # вводим ответ
    answer.send_keys(y)

    # кликаем checkbox и radiobutton
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # скроллим к кнопке и жмём Submit (на всякий случай)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(30)
    browser.quit()