import os
import time

from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    name = browser.find_element_by_xpath('//*[@name="firstname"]')
    name.send_keys('Анек')
    surname = browser.find_element_by_xpath('//*[@name="lastname"]')
    surname.send_keys('228')
    email = browser.find_element_by_xpath('//*[@name="email"]')
    email.send_keys('228@ya.ru')
    file_field = browser.find_element_by_xpath('//input[@type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_field.send_keys(file_path)
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
