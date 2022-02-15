from selenium import webdriver

import math
import time


def calc(x):
    return str(str(math.log(abs(12 * math.sin(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser.get(link)
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()