from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
# imprort os
import time 
import glob
from faker import Faker
import random

driver=webdriver.Chrome("./chromedriver")
fake = Faker()
n = int(input("number of blogs"))
url = "https://restful--blog.herokuapp.com/blogs/new"

with driver as dv:
    dv.get(url)
    dv.set_window_size(500, 500)
    # dv.maximize_window()
    for i in range(n):
        titletxt=fake.name()
        # imgtxt="https://picsum.photos/id/"++"/300/200"
        imgtxt= "https://picsum.photos/id/"+str(random.randint(0,800)) +"/300/200"
        desctxt=fake.text()

        title = dv.find_element(By.ID, 'title')
        title.send_keys(titletxt)
        imgurl = dv.find_element(By.ID, 'imgurl')
        imgurl.send_keys(imgtxt)
        desc = dv.find_element(By.ID, 'desc')
        desc.send_keys(desctxt)
        submitBtn = dv.find_element(By.ID, 'submitBtn')
        time.sleep(5)
        submitBtn.click()
        
        # newBlog = dv.find_element(By.ID, 'newBlog')

        time.sleep(5)
        dv.get(url)
        # newBlog.click()
        # driver.Navigate().GoToUrl(url)
        print(i)
    print(f"added {n} blogs to web")

    time.sleep(10)
