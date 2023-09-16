import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By

# Webdriver/actual
driver = webdriver.Chrome()



driver.get("https://demoqa.com/text-box")
driver.maximize_window()
# driver.implicitly_wait(15)


t =2
time.sleep(t)

nom=driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Mica Monje")
nom.send_keys(Keys.TAB)
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("mica.monje@nada.com")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("jsjdaksdoasdklaiwjeinqokw")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("jsjdaksdoasddasdadwwwwww")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR, "#submit").click()
time.sleep(t)



#Forma de llamar al implicity_wait
# driver.implicitly_wait(2)
# # driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
# # driver.find_element(By.ID, "adder").click()
# #
# # added = driver.find_element(By.ID, "box0")