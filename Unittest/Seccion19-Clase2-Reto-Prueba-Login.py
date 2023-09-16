import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class pruebaLogin(unittest.TestCase):

    # Primero debemos crear dos funciones base.son siempre estas
    def setUp(self):

        self.driver = webdriver.Chrome()

        #self.driver = (webdriver.Firefox())

    def test_Login1(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH , "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH , "//input[contains(@id,'login-button')]")
        nom.send_keys("Mica")
        pas.send_keys("RG2023")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        error = error.text
        if (error=="Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos")
            print("Pueba Ok")
        print(error)
        time.sleep(3)

    def test_Login2(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH , "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH , "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        pas.send_keys("RG2023")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        if (error=="Epic sadface: Username is required"):
            print("Faltan Datos")
            print("Pueba dos Ok")
        print(error)
        time.sleep(3)

    def test_Login3(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH , "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH , "//input[contains(@id,'login-button')]")
        nom.send_keys("Mica")
        pas.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        error = error.text
        if (error=="Epic sadface: Password is required"):
            print("Falta Contraseña")
            print("Pueba tres Ok")
        print(error)
        time.sleep(3)

    def test_Login4(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH , "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH , "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        pas.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        error = error.text
        if (error=="Epic sadface: Password is required"):
            print("Falta Ambos Campos")
            print("Pueba cuatro Pendiente")
        print(error)
        time.sleep(3)

    def test_Login5(self):
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH , "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH , "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        pas.send_keys("secret_sauce")
        btn.click()
        # error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        # error = error.text
        # if (error=="Epic sadface: Password is required"):
        #     print("Falta Contraseña")
        #     print("Pueba tres Ok")
        # print(error)
        time.sleep(3)


    def tearDown(self):
        driver = self.driver
        self.driver.close()
        time.sleep(4)



if __name__ == "__main__" :
    unittest.main()