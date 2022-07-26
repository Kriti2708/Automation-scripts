import time

from selenium import webdriver

driver = webdriver.Edge()

# First Tab
driver.get("https://www.google.com")
time.sleep(2)

# Second Tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
time.sleep(2)
driver.get('https://www.redbus.com')
time.sleep(4)

driver.close()

driver.quit()
