import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("partial_link",
                         ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_alien(browser, partial_link):
    link = f"https://stepik.org/lesson/{partial_link}/step/1"
    browser.get(link)
    text_area = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea")))
    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
    )
    button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='attempt-message_correct']"))
    )
    optional_feedback = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']").text
    assert optional_feedback == 'Correct!', optional_feedback
