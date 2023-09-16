import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class funcionesGlobales():
    # Sirve para inicializar funciones
    def __init__(self, driver):
        self.driver = driver

    #Funcion que devuelve valor Tiempo
    def GetTime(self, Tiempo):
        t = time.sleep(Tiempo)
        return t

    # Funcion para navegar/url
    def OpenPage(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina abierta " + str(Url))
        t = time.sleep(Tiempo)

#------------------------ Mixto -------------------------#
    def TextMixto(self, tipo, selector, texto, tiempo):
        if(tipo=="Xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto --> {}".format(selector,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
        elif (tipo=="ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.find_element(By.ID, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto --> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    def clickMixto(self, tipo, selector, tiempo):
        if(tipo=="Xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                print("Dando click en --> {}".format(selector,selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
        elif (tipo=="ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print("Dando click en --> {}".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
    # ------------------------------------ Funciones Mixta Mejoradas--------------------------------------------------------
    def SEXpath(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_xpath(elemento)
        return val

    def SEId(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_id(elemento)
        return val

    def SEMixto(self, tipo, selector, texto, tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento " + selector)
                return t
# -------------------------- XPATH ------------------------------------ #
    def TextXpath_Validar(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto --> {}".format(xpath, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def clickXpath_Validar(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Damos click en el campo --> {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)



    def SelectXpath(self, xpath, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El campo Seleccion es --> {}".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def UploadXpath(self, xpath, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("El campo Seleccion es --> {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def checkXpath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Click en el campo --> {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def checkXpathMultiples(self, tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("Click en el elemento --> {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento" + num)



# ------------------------------ ID ------------------------------------------- #

    def TextID_Validar(self, ID, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID, ID)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto --> {}".format(ID, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + ID)


    def clickID_Validar(self, ID, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID, ID)
            val.click()
            print("Damos click en el campo --> {}".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + ID)

    def SelectID(self, ID, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID, ID)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El campo Seleccion es --> {}".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + ID)

    def UploadID(self, ID, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID, ID)
            val.send_keys(ruta)
            print("El campo Seleccion es --> {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + ID)

    def checkID(self, ID, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.find_element(By.ID, ID)
            val.click()
            print("Click en el campo --> {}".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + ID)
            return t

# ---------------------------- SALIDA ------------------------------------------- #
    def salida(self):
        print("Se termina la prueba Exitosamente")

# ---------------------------- Funciones de botones ----------------------------------------#
    def MouseDoble(self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_xpath(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element_by_id(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t



    def MouseDerecho(self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val=self.SEX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val=self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def MouseDragDrop(self, tipo, selector, destino, tiempo=.2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val2 = self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

# ------------------------- Funciones de botones con coordenadas ----------------------------------------#

    def Mouse_DragDropXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                # self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                # self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

# -------------------------------------------------------------------------------- #


    #Primeras funciones

    #Funcion para texto path
    # def TextPath(self, Xpath, Text , Tiempo):
    #     val = self.driver.find_element(By.XPATH,(Xpath))
    #     val.clear()
    #     val.send_keys(Text)
    #     t = time.sleep(Tiempo)
    #     return t

    # Funcion para texto por ID
    # def TextID(self, ID, Text, Tiempo):
    #     val = self.driver.find_element(By.ID, (ID))
    #     val.clear()
    #     val.send_keys(Text)
    #     t = time.sleep(Tiempo)
    #     return t

    # # Funcion Click Xpath
    # def clickXPath(self, Xpath, Tiempo):
    #     val = self.driver.find_element(By.XPATH, (Xpath))
    #     val.click()
    #     t = time.sleep(Tiempo)
    #     return t
    #
    # # Funcion Click ID
    # def clickID(self, ID, Tiempo):
    #     val = self.driver.find_element(By.ID, (ID))
    #     val.click()
    #     t = time.sleep(Tiempo)
    #     return t
    #
    # def SelectXpath_Text(self, xpath, texto, tiempo):
    #     try:
    #         val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #         val = self.driver.find_element(By.XPATH, xpath)
    #         val = Select(val)
    #         val.select_by_visible_text(texto)
    #         print("El campo Seleccion es --> {}".format(texto))
    #         t = time.sleep(tiempo)
    #         return t
    #     except TimeoutException as ex:
    #         print(ex.msg)
    #         print("No se encontro el elemento" + xpath)
    #
    # def SelectID_Text(self, ID, texto, tiempo):
    #     try:
    #         val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
    #         val = self.driver.find_element(By.ID, ID)
    #         val = Select(val)
    #         val.select_by_visible_text(texto)
    #         print("El campo Seleccion es --> {}".format(texto))
    #         t = time.sleep(tiempo)
    #         return t
    #     except TimeoutException as ex:
    #         print(ex.msg)
    #         print("No se encontro el elemento" + ID)