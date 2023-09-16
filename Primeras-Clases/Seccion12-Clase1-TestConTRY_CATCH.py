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

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = 2

try:
    diaSelect = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))
    ds = Select(diaSelect)
    ds.select_by_visible_text("Monday")
    time.sleep(t)
    ds.select_by_index(5)
    time.sleep(t)
    ds.select_by_value("Sunday")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("No se encontro el elemento")

# finally:
#     driver.quit()

ciu = Select(driver.find_element(By.ID, "multi-select"))
ciu.select_by_index(2)
time.sleep(t)

ciu.select_by_index(4)
time.sleep(t)

ciu.select_by_index(6)
time.sleep(t)

time.sleep(t)
driver.close()
