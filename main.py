from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
time.sleep(10)