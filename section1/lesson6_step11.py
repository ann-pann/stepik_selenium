from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .first_class input')
    input1.send_keys('228')
    input2 = browser.find_element_by_css_selector('.first_block .second_class input')
    input2.send_keys('228')
    input3 = browser.find_element_by_css_selector('.first_block .third_class input')
    input3.send_keys('228')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(10)
    browser.quit()
