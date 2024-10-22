from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from trio import current_time
import time
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager


# Initialize the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to a specific URL
website_url=driver.get("https://katalon-demo-cura.herokuapp.com/")  # Replace with your desired URL
#driver.minimize_window()
#time.sleep(5)

# driver.get(website_url)
# time.sleep(3)

driver.maximize_window()

driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']").click()
driver.find_element(By.XPATH, "//input[@id='txt-username']").send_keys("John Doe")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@id='txt-password']").send_keys("ThisIsNotAPassword")
time.sleep(3)
hello=driver.find_element(By.XPATH,"//button[@id='btn-login']")
hello.click()

# alert=driver.switch_to.alert
# alert.accept()

# Handling any alert pop-ups
try:
    alert = driver.switch_to.alert
    alert.accept()  # This will accept the pop-up if it's a JavaScript alert
    print("Alert accepted.")
except:
    print("No alert found or the alert is not a JavaScript alert.")

    time.sleep(4)

 #For Drop Down meanu in the case of indexing

element = driver.find_element(By.XPATH, "//select[@id='combo_facility']")
drp = Select(element)
drp.select_by_index(2)
time.sleep(3)


#IN the case of check box
checkbox= driver.find_element(By.XPATH, "//input[@id='chk_hospotal_readmission']")
if checkbox.is_selected():
    pass
else:
    checkbox.click()
    time.sleep(3)

#Radio Button//label[normalize-space()='Medicare'

radio=driver.find_element(By.XPATH, "//label[normalize-space()='Medicaid']")
if radio.is_selected():
 pass
else:
 radio.click()
time.sleep(2)#driver.find_element(By.NAME, "username").send_keys("Admin")
#driver.find_element(By.NAME, "password").send_keys("admin123")


#if you have Name, id , you can use in this way otherwise go for relative path as below;
#driver.find_element(By.NAME, "login").click()


# This is the case when i dont have both name and id so i am going with relative path.
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Don't forget to close the driver when done
#driver.quit()
# calender

driver.find_element(By.XPATH, "//input[@id='txt_visit_date']").click()
time.sleep(4)













