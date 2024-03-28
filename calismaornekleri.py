from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.apple.com/")
link = driver.current_url
baslik = driver.title
print("ŞUANKİ BAŞLIK: "+baslik)
if "apple.com" in link:
    print("Doğru Apple sayfasındayiz: "+link)
driver.get("https://www.etsy.com/")
link = driver.current_url
baslik = driver.title
print("ŞUANKİ BAŞLIK: "+baslik)
if "etsy.com" in link:
    print("Etsy sayfasındayız: "+link)
sleep(3)
driver.back()
baslik = driver.title
driver.save_screenshot("./selenıum.png")
if "Apple"in baslik:
    print ("Tebrikler. Apple sayfasına döndün")

driver.quit()
