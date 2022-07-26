import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()

        link = 'http://suninjuly.github.io/registration1.html'
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        input1.send_keys('228')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        input2.send_keys('228')
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        input3.send_keys('228')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

        time.sleep(10)
        browser.quit()

    def test_2(self):
        browser = webdriver.Chrome()

        link = 'http://suninjuly.github.io/registration2.html'
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        input1.send_keys('228')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        input2.send_keys('228')
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        input3.send_keys('228')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
