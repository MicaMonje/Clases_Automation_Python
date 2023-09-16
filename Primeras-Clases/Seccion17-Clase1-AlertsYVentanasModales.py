import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Webdriver/actual
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

t = 2
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
time.sleep(t)

# Alerta -->
driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)

# Ejecuta el boton aceptar
driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]").click()

# Para ejecutar el boton close
#driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Close')])[1]").click()


time.sleep(4)
driver.close()