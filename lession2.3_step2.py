from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # нажимаем кнопку (откроется новая вкладка)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # считываем x и считаем ответ
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # вводим ответ и отправляем форму
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()