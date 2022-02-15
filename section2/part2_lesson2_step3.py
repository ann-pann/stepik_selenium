import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects2.html'

try:
    browser.get(link)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    num_sum = num1 + num2
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(num_sum))
    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
