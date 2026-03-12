from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    # обязательные поля
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Matvey")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Molodec")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@test.com")

    # отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    # проверка успешной регистрации
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(5)
    browser.quit()