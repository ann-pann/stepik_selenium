import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/math.html'
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    y = calc(x_element.text)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))

    robot_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot_checkbox.click()

    robot_radio_button = browser.find_element_by_css_selector("[for='robotsRule']")
    robot_radio_button.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
