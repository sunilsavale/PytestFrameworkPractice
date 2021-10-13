'''Concept of set -up and tear down method'''
'''fixtures concept'''
'''you can generat the html report '''
'''you need to installl the package like pip install pytest-html'''
'''enter the commmand in the command line llike pytest filename -v -s --html=filenamenot include test_and then _report.html'''
'''it will generate the html report and copy path and paste it at browser'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


'''Creating a global driver for set-up method which will work globally'''
'''create set up method'''

driver = None   #Create a driver for globally

def setup_module(module):

    global driver           #Make it globally
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://data-flair.training/courses/python-course/")


'''Creating the tear down method'''


def teardown_module(module):
    driver.quit()

'''creating a test cases here'''
def test_title():
    assert driver.title == "Python Course - DataFlair"

def test_url():
    assert driver.current_url == "https://data-flair.training/courses/python-course/"

