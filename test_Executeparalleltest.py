'''use of @pyest.mark.'name of test case' we can execute the particular test case '''
'''using py.test -n 4or5 this command to command line for executing the parallel mode '''
#code by sunil
#date 12/10/2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


#How to execute the parallel test case
#@pytest.mark.facebook


def test_facebook():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://meesho.com/")
    assert driver.title == "Meesho online shopping"
    print("title is not correct")
    driver.quit()


def test_input():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("Automation")
    driver.quit()

#@pytest.mark.facebook
def test_search():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("YouTube")
    driver.quit()



def test_login():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.reddit.com/")
    assert driver.title ==  "Reddit - Dive into anything"
    driver.quit()
