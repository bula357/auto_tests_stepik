from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

name = "Alex"
lastName = "Popov"
email = "alex_popov@gmail.com"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys(name)
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys(lastName)
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "[name='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла