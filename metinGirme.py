from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.duckduckgo.com/")
aramakutusu=driver.find_element(By.ID, "searchbox_input")
aramakutusu.send_keys("python")
sleep(2)
aramakutusu.click()
sleep(5)


