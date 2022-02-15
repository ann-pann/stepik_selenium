import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(link)

    chest_element = browser.find_element_by_xpath("//img[@src='images/chest.png']")
    x = chest_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(str(y))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    robot_radio_button = browser.find_element_by_id('robotsRule')
    robot_radio_button.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
