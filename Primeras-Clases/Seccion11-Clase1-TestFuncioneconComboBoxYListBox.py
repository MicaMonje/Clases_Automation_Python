import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Webdriver/actual
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

t = 2
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

# dias = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))
diaSelect = driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")
# -------- Seccion por partes --------
ds = Select(diaSelect)
# Por texto visible en el dropdown ()
ds.select_by_visible_text("Monday")
time.sleep(t)

# Por index si el texto cambiara (RECOMENDADO)
ds.select_by_index(5)
time.sleep(t)

# Por valor asignado en el codigo (SEGUNDO RECOMENDADO)
ds.select_by_value("Sunday")
time.sleep(t)

# ------------------ Tod@ en una seccion -------

ciu = Select(driver.find_element(By.ID, "multi-select"))
ciu.select_by_index(2)
time.sleep(t)

ciu.select_by_index(4)
time.sleep(t)

ciu.select_by_index(6)
time.sleep(t)

time.sleep(t)
driver.close()