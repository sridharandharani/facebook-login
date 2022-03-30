from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started ")
driver.get("https://www.w3schools.com/")
time.sleep(2)
driver.find_element_by_link_text("Tutorials").click()
time.sleep(3)
driver.find_element_by_link_text("Learn Java").click()
time.sleep(5)
driver.close()
print("Test close")