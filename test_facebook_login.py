from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started ")

driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("dharansri916@gmail.com")
time.sleep(2)
driver.find_element_by_name("pass").send_keys("dharansri916@")
time.sleep(2)
driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("testcase completed")
