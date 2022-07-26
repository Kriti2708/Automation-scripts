from selenium import webdriver

# CHROME
driver = webdriver.Chrome()
# First Tab
driver.get("https://www.google.com")
print(driver.title)
driver.save_screenshot("./screenshots/google.png")
# Second Tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://www.redbus.com')
print(driver.title)
driver.save_screenshot("./screenshots/redbus.png")
print('Chrome_Browser :: ' + driver.capabilities['browserVersion'])

driver.close()
driver.quit()
# FIREFOX
driver = webdriver.Firefox()
# First Tab
driver.get("https://www.google.com")
print(driver.title)
# Second Tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://www.redbus.com')
print(driver.title)
print('Firefox_Browser :: ' + driver.capabilities['browserVersion'])
print("platform Name ::  " + driver.execute_script("return navigator.platform;"))
driver.close()
driver.quit()
# EDGE
driver = webdriver.Edge()
# First Tab
driver.get("https://www.google.com")
print(driver.title)
# Second Tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://www.redbus.com')
print('Edge_Browser :: ' + driver.capabilities['browserVersion'])
print(driver.title)
driver.close()
driver.quit()
