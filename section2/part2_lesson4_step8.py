from selenium import webdriver

import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(str(math.log(abs(12 * math.sin(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button = browser.find_element_by_id('book')
    book_button.click()
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
