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

driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.maximize_window()
#driver.implicitly_wait(10)
t = 4

try:
    Buscar = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://Users//Panda//PycharmProjects//curso-QAAutoconPython//imagenes//gatete-demo.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH ,"//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("No se encontro el elemento")



time.sleep(t)
driver.close()