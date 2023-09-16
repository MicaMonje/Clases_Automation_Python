import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver/actual
driver = webdriver.Chrome()



driver.get("https://www.lambdatest.com/?fp_ref=devendra69")
driver.maximize_window()
#driver.implicitly_wait(10)
#
# t= 5
#
# btn= webdriver(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//p[contains(.,'See how 2 Million+ QAs and Devs accelerate their release cycles with LambdaTest.')]")))
# btn.click()
driver.find_element(By.XPATH,"").send_keys("Hola" + Keys.TAB + Keys.ENTER)
time.sleep(t)
driver.close()