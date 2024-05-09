import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		#CHROMEDRIVER
		service = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\chromedriver.exe")
		self.driver = webdriver.Chrome(service=service)
		#EDGEDRIVER
		#service = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe")
		#self.driver = webdriver.Edge(service=service)

	def test_buscar_por_nombre(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		buscar_por_nombre = driver.find_element(By.NAME, "q")
		time.sleep(3)
		buscar_por_nombre.send_keys("selenium", Keys.ARROW_DOWN)
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()

#Xpath=//Etiqueta[@atributo='valor']
#XPath absoluto ejemplo /html/body/div/div/div/article[2]/div/div/a/img, el inconveniente con este xpath es que si se cambia algo en la ruta ya no se podra encontrar
#Xpath relativo ejemplo //*[@id="q"], la ventaja que se puede encontrar en cualquier parte del codigo ya que parte de un nodo y no de la raiz

