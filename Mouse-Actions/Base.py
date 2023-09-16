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
from selenium.webdriver import ActionChains


class baseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Login1(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.OpenPage("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        f.TextMixto("Xpath", "//input[contains(@class,'oxd-input oxd-input--focus')]", "Admin", 2)
        f.TextMixto("Xpath", "//input[contains(@class,'oxd-input oxd-input--active')]", "admin123", 2)
        f.clickMixto("Xpath", "//button[@type='submit'][contains(.,'Login')]", 2)

        f.GetTime(4)
        admin = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item active")
        sub1 = driver.find_element(By.CLASS_NAME,"oxd-topbar-body-nav-tab-item")
        sub2 = driver.find_element(By.CLASS_NAME, "oxd-topbar-body-nav-tab-link")

        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()

