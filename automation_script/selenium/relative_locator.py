import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

print("This is title - ", driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys("abcd")
time.sleep(1)
password = driver.find_element(locate_with(By.TAG_NAME, "input").below(email))
password.send_keys("1234")

# driver.quit()
