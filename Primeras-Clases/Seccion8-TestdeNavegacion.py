import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By

# Webdriver/actual
driver = webdriver.Chrome()

#variable tiempo general
t= 2

# dir ijo a la pag
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.selenium.dev/documentation/webdriver/elements/")
time.sleep(t)

driver.get("https://www.deepl.com/es/translator#en/es/")
time.sleep(t)

#sirve para restar o sumar tiempo
driver.execute_script("window.history.go(-1)")

driver.execute_script("window.history.go(-1)")

#Utilizado para controlar el boton de regreso/avance del navegador
#driver.forward()
driver.execute_script("window.history.go(1)")
time.sleep(t)