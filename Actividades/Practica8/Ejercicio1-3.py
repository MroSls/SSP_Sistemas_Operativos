import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abrir el navegador
class usando_unittest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()

    def test_buscar(self):
        self.driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=_eeS24nuHUm_P6918HPgz8kGucio5uRAucnQjmvXLKJUNURCSlVMNDg4RTBQRk9JNkhYMEFSUFJMOS4u")

        # Wait for the form to load
        wait = WebDriverWait(self.driver, 10)
        form = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='formContainer']")))

        # Fill in the input elements
        input_elements = form.find_elements(By.XPATH, "//input[@type='text']")
        for element in input_elements:
            element.send_keys("Test Value")

        # Fill in the textarea element
        textarea_element = form.find_element(By.XPATH, "//textarea[@id='textareaQuestion']")
        textarea_element.send_keys("This is a test message.")

        # Submit the form
        submit_button = form.find_element(By.XPATH, "//input[@type='submit']")
        #submit_button.click()

        # Verify that the form submission was successful
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='thankyou-message']")))
        self.assertIn("Gracias por su respuesta", success_message.text)

if __name__ == "__main__":
    unittest.main()
