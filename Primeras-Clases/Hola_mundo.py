from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Webdriver/actual
driver = webdriver.Chrome()

# dir ijo a la pag
driver.get("https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwievtfKuomBAxWbpZUCHWs9DQAQPAgJ")
print("Bienvenido a selenium")
print(driver.title)

# cie rra pag
driver.close()
