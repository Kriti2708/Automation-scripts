import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://github.com/")
driver.maximize_window()
time.sleep(2)

# sign in - it should redirect to the login page
sign_in = driver.find_element(By.XPATH, value="//a[contains(text(),'Sign in')]")
sign_in.click()
time.sleep(2)

# loging in with credentials
username = driver.find_element(By.XPATH, value="//input[@id='login_field']")
username.send_keys("kriti.baghel27@gmail.com")
password = driver.find_element(By.XPATH, value="//input[@id='password']")
password.send_keys("9300961977k")
time.sleep(2)

button = driver.find_element(By.XPATH, value="//body/div[3]/main[1]/div[1]/div[4]/form[1]/div[1]/input[12]")
button.click()
time.sleep(4)

# Verify github logo
git_logo = driver.find_element(By.XPATH, value="//header/div[1]/a[1]/*[1]")
git_logo.click()
time.sleep(5)

# creating new repo - it will redirect on the create repository page
create_repo = driver.find_element(By.XPATH, value="//div[@class='dashboard-sidebar top-0 px-3 px-md-4 px-lg-5 "
                                                  "overflow-auto']//a[@class='btn btn-sm btn-primary']["
                                                  "normalize-space()='New']")
create_repo.click()
time.sleep(3)

# redirecting to home page
git_logo = driver.find_element(By.XPATH, value="//header/div[1]/a[1]/*[1]")
git_logo.click()
time.sleep(5)

# open existing repo
repo = driver.find_element(By.XPATH, value="//aside[@aria-label='Account']//li[1]//div[1]//div[1]//a[1]")
repo.click()
time.sleep(2)

git_logo = driver.find_element(By.XPATH, value="//header/div[1]/a[1]/*[1]")
git_logo.click()
time.sleep(2)

# signing out - opening the dropdown and then clicking the sign-out
dropdown = driver.find_element(By.XPATH, value="")
dropdown.click()

sign_out = driver.find_element(By.XPATH, value="")
sign_out.click()

time.sleep(5)
driver.close()
