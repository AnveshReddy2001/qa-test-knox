from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://172.26.48.148:31233/")

frontend = driver.find_element(By.XPATH, "/html/body/h1").text
backend = "Hello from the Backend!"

if frontend == backend:
    print("Test is passed")
else:
    print("Test is failed")

driver.quit()
