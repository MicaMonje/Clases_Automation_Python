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

t = 3
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

btn = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
btn.click()
# print(btn.is_enabled())
time.sleep(t)

# ---------------------------- Nombre ------------------------
name_val = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
# Le decimos que nos guarde el texto
name = name_val.text
#print("El valor del error es: " + name)

# Condicionante
if (name == "Please supply your first name"):
    cn = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]")
    cn.send_keys("Micaela")
    print("Nombre correcto")
    time.sleep(t)
else:
    print("Falta el nombre")

# ----------------------------- Apellido ---------------------
ap_val = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")
# Le decimos que nos guarde el texto
ape = ap_val.text
#print("El valor del error es: " + name)

# Condicionante
if (ape == "Please supply your last name"):
    apel = driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]")
    apel.send_keys("Monje")
    print("Apellido correcto")
    time.sleep(t)
else:
    print("Falta el Apellido")

print(btn.is_enabled())

if (btn.is_enabled()==False):
    print("Faltan campos para llenar")
else:
    print("Esta todo correcto")

time.sleep(t)
driver.close()