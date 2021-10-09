'''Pytest Basics'''
# code by sunil
# date - 9/10/2021

import pytest


'''1) Test methods and classes can be marked, and tagnames can be customized. 
2) It is better to have meaningful names
3) The same test class / method can have multiple tags at the same time'''
@pytest.mark.login
def test_1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not eq to b"

def test_2():
    name = "selenium"
    assert name.upper() == "SELENIUM"   # use of upper() case method

@pytest.mark.login
def test_3():
    assert True

def test_4():
    assert False
