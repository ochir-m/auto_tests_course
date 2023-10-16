import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    value_x = browser.find_element(By.ID, "input_value").text
    y = calc(value_x)
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
