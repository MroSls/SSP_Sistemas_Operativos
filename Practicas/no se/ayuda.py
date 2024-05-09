import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class usando_unittest(unittest.TestCase):
	def setUp(self):
		service = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe")
		self.driver = webdriver.Edge(service=service)
	def test_usando_select(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
		time.sleep(3)
		nombre = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[1]/td[2]/input")
		seleccionar = Select(driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div[1]/select"))
		seleccionar.select_by_value("C_T_ACTIVIDAD_PREST_SERV_ENERG")
	
		como = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[2]/td[2]/select")
		comoopcion = como.find_elements(By.TAG_NAME,"option")

		provincia = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[3]/td[2]/div/select")
		provinciaopcion = provincia.find_elements(By.TAG_NAME,"option")

		localidad = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[4]/td[2]/div/select")
		localidadopcion = localidad.find_elements(By.TAG_NAME,"option")

		linea = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[1]/td[4]/select")
		lineaopcion = linea.find_elements(By.TAG_NAME,"option")

		categoria = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[2]/td[4]/div/select")
		categoriaopcion = categoria.find_elements(By.TAG_NAME,"option")

		tipologia = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[3]/td[4]/div/select")
		tipologiaopcion = tipologia.find_elements(By.TAG_NAME,"option")

		actuaciones = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[4]/td[4]/div/select")
		actuacionesopcion = actuaciones.find_elements(By.TAG_NAME,"option")


if __name__ == '__main__':
	unittest.main()
