from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    # для проверки второго задания просто поменяй ссылку:
    # browser.get("https://suninjuly.github.io/selects2.html")

    # считываем числа
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    result = str(int(num1) + int(num2))  # ОБЯЗАТЕЛЬНО строка

    # работаем с выпадающим списком
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    # отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()