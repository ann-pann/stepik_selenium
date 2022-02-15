import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    robot_check = browser.find_element_by_xpath('//*[@for="robotCheckbox"]')
    robot_check.click()
    robot_radio = browser.find_element_by_xpath('//*[@for="robotsRule"]')
    robot_radio.click()
    button = browser.find_element_by_xpath('//*[@type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
