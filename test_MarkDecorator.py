'''use of @pytest.mark'''
'''test will execute by marker'''
# code by sunil savale
# date - 14-10-2021
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


# launch the browser and create a test case
@pytest.mark.check
def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.selenium.dev/documentation/webdriver/")
    print(driver.title)


def test_search():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("facebook")
    print(driver.title)


def test_logoff():
    print("sign off")


def test_logout():
    print("log out from the")


@pytest.mark.check
def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("instagram")
    print(driver.title)