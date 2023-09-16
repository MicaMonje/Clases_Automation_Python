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
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

# Lo declaramos como variable para llamarlo mas facil en el IF

btn = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(btn.is_enabled())

#
if (btn.is_enabled()==True):
    print("Puedes hacerle click")

else:
    print("No existe, no puedes ingresar")



time.sleep(t)
driver.close()