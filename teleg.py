import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger
from selenium import webdriver

import time

def get_count_input():
    count_input = askinteger("Input", "Enter count:")
    return count_input
def get_user_input():
    user_input = askstring("Input", "Enter your number:")
    return user_input

count = get_count_input()

for i in range(count):
    driver = webdriver.Chrome()
    driver.get("https://web.telegram.org/a/")

    time.sleep(4)

    log_in = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/button[1]")
    log_in.click()
    time.sleep(3)

    inputNumber = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div/div/form/div[2]/input")
    inputNumber.send_keys(get_user_input())
    time.sleep(2)

    auth = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div/div/form/button[1]/div")
    auth.click()
    time.sleep(3)