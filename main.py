import tkinter as tk
from tkinter.simpledialog import askstring

from selenium import webdriver

import time




def get_user_input():
    user_input = askstring("Input", "Enter your text:")
    return user_input


file_path = "C:\RRXmFKwk1ak.png"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome()
driver.get("https://xn-----6kcbl7bbwdfiqtgd.xn--p1ai/#zapis_na_SVO")




search_box = driver.find_element("name", "lastname")
search_box.send_keys(get_user_input())


input_field = driver.find_element("name", "name")
input_field.send_keys("awdwad")
input_field.submit()

input_field2 = driver.find_element("name", "secondname")
input_field2.send_keys("awdwad")
input_field2.submit()
element1 = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[10]/div/div/div/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/div/div/input")
element1.send_keys('123')
element1.submit()
input_field4 = driver.find_element("name", "phone")
input_field4.send_keys("+375297781673")
input_field4.submit()
element2 = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[10]/div/div/div/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/div/div/input")
element2.send_keys("awdawd")


input_photo = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[10]/div/div/div/div/div/div/div/div/div[2]/form/div[1]/div[7]/div/div/div[2]/div[1]/div[2]/label/input")
input_photo.send_keys(file_path)
time.sleep(2)
submit_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[10]/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div/button")
submit_button.click()
time.sleep(4)

