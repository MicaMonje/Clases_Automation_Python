import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import funcionesGlobales

class pageLogin():
    # Sirve para inicializar funciones
    def __init__(self, driver):
        self.driver = driver

    def loginMaster(self, url, name, clave):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.OpenPage(url, 1)
        f.TextXpath_Validar("//input[contains(@id,'user-name')]", name, 2)
        f.TextXpath_Validar("//input[contains(@id,'password')]", clave, 2)
        f.clickXpath_Validar("//input[contains(@id,'login-button')]", 2)

        f.salida()