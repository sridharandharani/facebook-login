from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone 11")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)
driver.find_element_by_partial_link_text("47,990").click()
time.sleep(5)
driver.close()
print("Test close")
