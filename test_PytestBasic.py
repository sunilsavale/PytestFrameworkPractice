
import pytest



#Learnig pytest
#Code by Sunil
#Date 30/09/2021


#we have to insatlled pytest package by using the pip install pytest command in the terminal or cmd of python
#We have to create a file in pytest it should start with the test_ or end with test_
#File name should be start with test keyword
#File name should br end with test keyword


#Test no.One
def test_t1():
    a = 3
    b = 9
    if a != b:
        print("a is not equal to b")


#Test No. Two
def test_t2():
    name = "sunil"
    assert name == "Sunil", "Both are not Equal"


#Test No. Three
def test_t3():
    assert True

#Test no. t4
def test_t4():
    assert False, "false test will failes always"


#Test No. t5
def test_t5():
    a = "Ravi"
    b = "Naveen"
    c = "Potter"

    if len(a) < len(b):
        print("Not more than the b")

    elif len(a) > len(b):
        print("a is less than b")

    elif len(b) != len(c):
        print("b len. is not equal to c")
