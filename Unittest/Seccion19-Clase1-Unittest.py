import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class base_test(unittest.TestCase):

    # Primero debemos crear dos funciones base.son siempre estas
    def setUp(self):

        self.driver = webdriver.Chrome()

        #self.driver = (webdriver.Firefox())

        print("hola")

    def test1(self):
        driver = self.driver
        self.driver.get("https://demoqa.com/text-box")
        self.driver.maximize_window()
        t = 3
        time.sleep(t)

    def tearDown(self):
        driver = self.driver
        self.driver.close()
        time.sleep(4)



if __name__ == "__main__" :
    unittest.main()