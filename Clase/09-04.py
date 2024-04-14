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
        self.driver.get("http://www.google.com")
        self.assertIn("Google", self.driver.title)


        elemento = self.driver.find_element(By.NAME, "q")

        elemento.send_keys("Selenium")
        elemento.send_keys(Keys.RETURN)


        time.sleep(20)


        assert "No se ha encontrado resultado" not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
