from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from faker import Faker
import random

fake = Faker()
n = int(input("how many fake blogs you wanna enter ?  "))

driver=webdriver.Chrome("./chromedriver")
url = "https://restful--blog.herokuapp.com/blogs/new"


driver.get(url)
driver.set_window_size(500, 500)
# dv.maximize_window()
for i in range(n):
    titletxt=fake.name()
    # imgtxt="https://picsum.photos/id/"++"/300/200"
    imgtxt= "https://picsum.photos/id/"+str(random.randint(0,800)) +"/300/200"
    desctxt=fake.text()
    title = driver.find_element(By.ID, 'title')
    title.send_keys(titletxt)
    imgurl = driver.find_element(By.ID, 'imgurl')
    imgurl.send_keys(imgtxt)
    desc = driver.find_element(By.ID, 'desc')
    desc.send_keys(desctxt)
    submitBtn = driver.find_element(By.ID, 'submitBtn')
    time.sleep(5)
    submitBtn.click()

    time.sleep(5)
    if i<=n+1:
        driver.get(url)
    # newBlog = dv.find_element(By.ID, 'newBlog')
    # newBlog.click()
    # driver.Navigate().GoToUrl(url)
    print(i)
print(f"added {n} blogs to web")
time.sleep(5)
driver.close()