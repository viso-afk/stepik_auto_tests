from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # нажимаем кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # принимаем confirm
    alert = browser.switch_to.alert
    alert.accept()

    # считываем x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()