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
driver.get("https://pixabay.com/")
driver.maximize_window()
time.sleep(t)

# Es un metodo para buscar pero no es el recomendado.
# driver.execute_script("window.scrollTo(0,1000)")


try:
    Buscar = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Discover more')]")))
    Buscar = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Discover more')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("No se encontro el elemento")



time.sleep(t)
driver.close()