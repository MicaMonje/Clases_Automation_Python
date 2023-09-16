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
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

# Obteniendo tod@ los links de la pagina
links = driver.find_elements(By.TAG_NAME, "a")
print("El numero de tag en la pag. son: ", len(links))

#Con esto decimos que recorra tod@s los elementos nos imprima tod@s los links en forma de texto
for num in links:
    print(num.text)

# Links test padres e hijos
driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)

time.sleep(t)
driver.close()