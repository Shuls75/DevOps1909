from selenium import webdriver
from time import sleep

d = webdriver.Chrome()


def my_test(values_to_check, expected):
    d.get("file:///D:/Documents/Shalom/Learning/DevOps 19.09.24/Lesson 4/tip_calc/index.html")
    d.find_element(by="id", value="billamt").send_keys(values_to_check[0])
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[2]').click()
    d.find_element(by="id", value="peopleamt").send_keys(values_to_check[1])
    d.find_element(by="xpath", value='//*[@id="musicQual"]/option[2]').click()
    actual = d.find_element(by="id", value="tip").text
    is_visible = d.find_element(by="id", value="tip").is_displayed()

    # Debugging print
    print(f"Actual: '{actual}'")

    assert actual == expected
    assert is_visible


my_test(["100", "5"], "5.60")
