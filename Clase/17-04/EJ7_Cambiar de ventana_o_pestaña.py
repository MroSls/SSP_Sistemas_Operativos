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

	def test_usando_select(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		driver.execute_script("window.open('');")
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[1])
		driver.get("http://stackoverflow.com")
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)

if __name__ == '__main__':
	unittest.main()