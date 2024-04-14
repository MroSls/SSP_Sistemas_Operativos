import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
    def test_buscar(self):
        self.driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=_eeS24nuHUm_P6918HPgz8kGucio5uRAucnQjmvXLKJUNURCSlVMNDg4RTBQRk9JNkhYMEFSUFJMOS4u")
        self.assertIn("Prueba selenium llenado", self.driver.title)
        Name = self.driver.find_element(By.XPATH,'//*[@id="question-list"]/div[1]/div[2]/div/span/input')
        Name.send_keys("Mario")
        LastName = self.driver.find_element(By.XPATH,'//*[@id="question-list"]/div[2]/div[2]/div/span/input')
        LastName.send_keys("Solis")
        career = self.driver.find_element(By.XPATH,'//*[@id="question-list"]/div[3]/div[2]/div/span/input')
        career.send_keys("Ing. en Computacion")
        Campus = self.driver.find_element(By.XPATH,'//*[@id="question-list"]/div[4]/div[2]/div/span/input')
        Campus.send_keys("Centro")
        time.sleep(10)
        Submit_Button = self.driver.find_element(By.XPATH,'//*[@id="form-main-content1"]/div/div/div[2]/div[2]/div/button')
        Submit_Button.click()
        time.sleep(10)
if __name__ == "__main__":
    unittest.main()