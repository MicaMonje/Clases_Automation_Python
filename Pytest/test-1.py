import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import funcionesGlobales
from selenium.webdriver import ActionChains

def testLogin1():
    global driver
    driver = webdriver.Chrome()
    f = funcionesGlobales(driver)
    f.OpenPage("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    f.TextMixto("Xpath", "//input[contains(@id,'Email')]", "mica123@gmail.com", 2)
    f.TextMixto("Xpath", "//input[contains(@id,'Password')]", "123456", 2)
    f.clickMixto("Xpath", "//button[@type='submit'][contains(.,'Log in')]", 2)
    e1 = f.SEId("//div[@class='message-error validation-summary-errors']")
    e1 = e1.text
    print(e1)
    if(e1=="No customer account found"):
        print("Prueba de validacion exitosa")
    else:
        print("La prueba es incorrecta")

def testLogin2():
    global driver
    driver = webdriver.Chrome()
    f = funcionesGlobales(driver)
    f.OpenPage("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    f.TextMixto("Xpath", "//input[contains(@id,'Email')]", "", 2)
    f.TextMixto("Xpath", "//input[contains(@id,'Password')]", "123456", 2)
    f.clickMixto("Xpath", "//button[@type='submit'][contains(.,'Log in')]", 2)
    e1 = f.SEXpath("//span[contains(@id,'Email-error')]")
    e1 = e1.text
    print(e1)
    if(e1=="Please enter your email"):
        print("Prueba de email vacio exitosa")
    else:
        print("La prueba de mail vacio es incorrecta")


