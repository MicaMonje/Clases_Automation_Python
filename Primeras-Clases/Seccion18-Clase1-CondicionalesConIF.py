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
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

# Lo declaramos como variable para llamarlo mas facil en el IF

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

# Se utiliza para verificar que se este devolviendo un elemento --> Verifica que un elemento sea visible
print(titulo.is_displayed())
btn1 = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

# Si el elemento es igual a true devolveme ".."
if (titulo.is_displayed()==True):
    print("La imagen si existe")
    btn1.click()
    time.sleep(t)

# Si el elemento no existe devolveme "..."
else:
    print("No existe la imagen")

time.sleep(t)
driver.close()