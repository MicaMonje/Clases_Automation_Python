import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver/actual
#driver = webdriver.Chrome()
driver = webdriver.Firefox()

t = 5
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
#driver.implicitly_wait(10)

btn1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn1.click()

btn5 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[5]")))
btn5.click()

btn6 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[6]")))
btn6.click()

# driver.find_element(By.XPATH,"").send_keys("Hola" + Keys.TAB + Keys.ENTER)
# time.sleep(t)

time.sleep(t)
driver.close()
