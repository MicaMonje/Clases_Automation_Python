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

t = .5
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

try:
    driver.execute_script("window.scrollTo(0,300)")
    nombre = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Micaela")
    ape = driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("Monje")
    email = driver.find_element(By.XPATH, "//input[contains(@name,'email')]").send_keys("Mica.m.m@gmail.com")
    cel = driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("3834569878")
    correo = driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("AV. Gata Gorda 123")
    ciuda = driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Argentina")
    estado = Select(driver.find_element(By.XPATH, "//select[contains(@name,'state')]")).select_by_visible_text("Alaska")
    codigo = driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("99501")
    dominio = driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys("https://pixabay.com/illustrations/")
    check = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'yes')]")))
    check.click()
    description = driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("bla bnlaijosajdmasdoijapsdpjasjd asdoasd")
    driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]").click()

except TimeoutException as ex:
    print(ex.msg)
    print("No se encontro el elemento")


time.sleep(t)
driver.close()

