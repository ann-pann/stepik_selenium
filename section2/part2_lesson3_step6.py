from selenium import webdriver

import math
import time


def calc(x):
    return str(str(math.log(abs(12 * math.sin(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser.get(link)
    redirect_button = browser.find_element_by_xpath('//button[@type="submit"]')
    redirect_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()