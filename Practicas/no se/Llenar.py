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
		driver.get("https://incentivos.agenciaandaluzadelaenergia.es/Orden2016SIG/listado.jsp")
		time.sleep(3)
		nombre = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[1]/td[2]/input")
		
		como = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[2]/td[2]/select")

		provincia = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[3]/td[2]/div/select")

		localidad = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[4]/td[2]/div/select")

		linea = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[1]/td[4]/select")

		categoria = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[2]/td[4]/div/select")

		tipologia = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[3]/td[4]/div/select")

		actuaciones = driver.find_element(By.XPATH,"/html/body/div[1]/form/center/table/tbody/tr[4]/td[4]/div/select")

		nombre.send_keys("Mamitas")

		seleccionarcomo = Select(como)
		seleccionarcomo.select_by_value("C_T_ACTIVIDAD_PREST_SERV_ENERG")
		#time.sleep(1)
		seleccionarprovincia = Select(provincia)
		seleccionarprovincia.select_by_value("BARCELONA")
		#time.sleep(1)
		seleccionarlocalidad = Select(localidad)
		seleccionarlocalidad.select_by_value("ALCALÁ DEL RÍO")
		#time.sleep(1)
		seleccionarlinea = Select(linea)
		seleccionarlinea.select_by_value("REDES INTELIGENTES")
		#time.sleep(1)
		seleccionarcategoria = Select(categoria)
		seleccionarcategoria.select_by_value("A.2. Mejora de la eficiencia energética y mayor contribución a la protección ambiental")
		#time.sleep(1)
		seleccionartipologia = Select(tipologia)
		seleccionartipologia.select_by_value("A.2.2. Mejora de las cogeneraciones existentes y promoción de la cogeneración de alta eficiencia")
		#time.sleep(1)
		seleccionaractuaciones = Select(actuaciones)
		seleccionaractuaciones.select_by_value("03PS")

		#boton = driver.find_element(By.XPATH,"/html/body/div[1]/form/input[1]")
		#boton.click()

		time.sleep(5)

if __name__ == '__main__':
	unittest.main()