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
from Funciones.PageLogin import pageLogin


class pruebaLogin(unittest.TestCase):

    # Primero debemos crear dos funciones base.son siempre estas
    def setUp(self):

        self.driver = webdriver.Chrome()

        #self.driver = (webdriver.Firefox())

    def test_Login1(self):
        driver = self.driver
        f = funcionesGlobales(driver)
        f.OpenPage("https://demoqa.com/text-box", 2)
        # pg = pageLogin(driver)
        # pg.loginMaster("https://www.saucedemo.com/v1/", "Micaela", "Monje")
        # f.SelectXpath_Text("//select[contains(@id,'select-demo')]", "Friday", 2)
        # f.SelectID("select-demo", "index", "4", 2)
        # f.UploadID("fileinput", "C://Users//Panda//PycharmProjects//curso-QAAutoconPython//imagenes//gatete-demo.jpg", 5)
        # f.checkID("isAgeSelected",2)
        # for n in range(2,5):
        #     f.checkXpathMultiples(3, "(//input[contains(@type,'checkbox')])["+str(n)+"]")
        f.TextMixto("ID", "userName", "micami",3)
        f.TextMixto("ID", "userEmail", "micami@sdasdasd.com", 3)
        f.TextMixto("ID", "currentAddress", "micami 123456", 3)
        f.TextMixto("ID", "permanentAddress", "asjdlkaskdlaksjdialk ksjdajslkdjad9qiweuqbfq9ejbau a98sdu09au9dhqwheqhw0e", 3)
        f.clickMixto("Xpath", "//button[contains(@id,'submit')]",3)



    # def tearDown(self):
    #     driver = self.driver
    #     self.driver.close()
    #     time.sleep(2)
#
#
#
if __name__ == "__main__" :
    unittest.main()