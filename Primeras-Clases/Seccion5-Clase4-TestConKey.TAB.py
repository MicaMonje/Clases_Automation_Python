import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By

# Webdriver/actual
driver = webdriver.Chrome()

# dir ijo a la pag
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Mica Monje")
nom.send_keys(Keys.TAB)
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("mica.monje@nada.com")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("jsjdaksdoasdklaiwjeinqokw")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("jsjdaksdoasddasdadwwwwww")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "#submit").click()
# time.sleep(5)

#Vacia campos para volver a rellenar
#driver.find_element(By.NAME, "email_input").clear()
#Como se usaria junto t0do
#driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev" )

driver.close()