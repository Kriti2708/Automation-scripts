import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://register.rediff.com/register/register.php?FormName=user_details')
driver.maximize_window()
# fullName
full_name = driver.find_element(By.XPATH, '//tbody/tr[3]/td[3]/input[1]')
full_name.send_keys("Kriti Baghel")
time.sleep(2)

# Reference id
reddif_id = driver.find_element(By.XPATH, '//tbody/tr[7]/td[3]/input[1]')
reddif_id.send_keys("krbaghel")
time.sleep(2)

# Availability of reference id
avail_button = driver.find_element(By.XPATH, '//tbody/tr[7]/td[3]/input[2]')
avail_button.click()
time.sleep(2)

# Password
password = driver.find_element(By.XPATH, '//tbody/tr[9]/td[3]/input[1]')
password.send_keys("Kb12345678")
time.sleep(2)

# Reenter password
retype = driver.find_element(By.XPATH, '//tbody/tr[11]/td[3]/input[1]')
retype.send_keys("Kb12345678")
time.sleep(2)

# Alternate email id
alt_email = driver.find_element(By.XPATH, '//tbody/tr[1]/td[3]/input[1]')
alt_email.send_keys("krbaghel@gmail.com")
time.sleep(2)

# Contact number
num = driver.find_element(By.XPATH, "//input[@id='mobno']")
num.send_keys("7898238827")
time.sleep(2)

# Date of Birth
day = Select(driver.find_element(By.XPATH, value='//tbody/tr[22]/td[3]/select[1]'))
day.select_by_index('4')
time.sleep(2)

month = Select(driver.find_element(By.XPATH, value='//tbody/tr[22]/td[3]/select[2]'))
month.select_by_visible_text('FEB')
time.sleep(2)

year = Select(driver.find_element(By.XPATH, value='//tbody/tr[22]/td[3]/select[3]'))
year.select_by_value('2019')
time.sleep(2)


# Gender
female = driver.find_element(By.XPATH, value='//tbody/tr[24]/td[3]/input[2]')
female.click()
time.sleep(2)

male = driver.find_element(By.XPATH, value='//tbody/tr[24]/td[3]/input[1]')
male.click()
time.sleep(2)

# Country
country = Select(driver.find_element(By.ID, value='country'))
country.select_by_visible_text('India')
time.sleep(2)

# City
city = Select(driver.find_element(By.XPATH, value='//tbody/tr[1]/td[3]/select[1]'))
city.select_by_visible_text('Agra')
time.sleep(2)

driver.save_screenshot('.\\kriti.png')

driver.close()
