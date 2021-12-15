from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button=browser.find_element(By.ID, "book")
    button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option2 = browser.find_element(By.ID, "solve")
    option2.click()
    print(browser.switch_to.alert.text)
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)
finally:
    time.sleep(5)
    browser.quit()