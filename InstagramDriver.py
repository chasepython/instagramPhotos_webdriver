# Intall ChromeDriver.exe which matchs your Chrome version. From "https://chromedriver.storage.googleapis.com/index.html". 
# If it was executed automatically,it would be easily interrupted by any movement. 
from selenium import webdriver
from selenium.webdriver.common import keys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import os
import wget
#------------------------------------------------------------------------------------------------------------------------------------------------------

path = "C:/ChromeDriver/ChromeDriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

username.clear()
password.clear()
username.send_keys("#####")    # Your UserName
password.send_keys("#####")    # Your Password

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()

keyword = "#####"   # "keyword" means what you want to search.

search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
search.clear()
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"FFVAD"))) 


path_file = os.path.join(keyword)  # Create Folder
os.mkdir(path_file)                # Create Path

srcs = []
count = 1
for i in range(10):

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    imgs = driver.find_elements_by_class_name("FFVAD")

    for img in imgs:
        x = img.get_attribute("src")
        srcs.append(x)

    time.sleep(2.5)             # Base on your internet speed. 2.5 seconds at least is better.

srcs = list(set(srcs))

for src in srcs:

    save_as = os.path.join(path_file,keyword + '_' + str(count) + '.jpg')  
    wget.download(src,save_as)
    count += 1

print("\n"+"Completed ! Total: "+str(len(srcs))+" photos")