#about pytest fixtures
'''the purpose of test fixture is to provide a fixed baseline upon which tests can reliably and repeatedly execute'''
#how will create a fixture in pytest is given below
'''@pytest.fixture():- Execute the specific method before every test method'''
'''@pytest.yield_fixture() :- Execute specifid method before and after every last method'''

#Code by sunil savale
#Date - 03-10-2021

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def SetUp():
    print("Before test method execute, SetUp method  will execute every time")
'''we need to pass the set up method in every test method'''
#test method 1
def test1(SetUp):
    #launch the browser
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    #navigate the URL
    driver.get("https://www.google.com/")
    print(driver.title)

#test method 2
def test2(SetUp):
    #launch the browser
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    #navigate the URL
    driver.get("https://www.google.com/")
    print(driver.title)
    driver.find_element_by_name("q").send_keys("facebook")
