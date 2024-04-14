import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        # Establece la ruta al ejecutable de Microsoft Edge WebDriver
        servicio = Service(executable_path=r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe")

        # Crea una instancia de Edge WebDriver
        self.driver = webdriver.Edge(service=servicio)

        # Maximiza la ventana del navegador para mejor visibilidad (opcional)
        self.driver.maximize_window()

    def test_buscar(self):
        # Navega a la URL objetivo (una página de Microsoft Forms)
        self.driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=_eeS24nuHUm_P6918HPgz8kGucio5uRAucnQjmvXLKJUNURCSlVMNDg4RTBQRk9JNkhYMEFSUFJMOS4u")

        # Afirma que el título de la página contiene "Prueba selenium llenado" (título esperado)
        self.assertIn("Prueba selenium llenado", self.driver.title)

        # Ubica el elemento de búsqueda usando su atributo de nombre (si aplica)
        elemento = self.driver.find_element(By.CLASS_NAME, "-nF-64")  # Reemplaza con el localizador apropiado si es necesario

        # Escribe "Selenium" en el elemento de búsqueda
        elemento.send_keys("Selenium")

        # Simula presionar la tecla Enter para enviar la búsqueda
        elemento.send_keys(Keys.RETURN)

        # Espera 5 segundos a que se carguen los resultados de la búsqueda (podría necesitar ajustes)
        time.sleep(5)

        # Afirma que "No se ha encontrado resultado" (que significa "No se encontraron resultados") no está presente en el código fuente de la página,
        # lo que indica que se muestran al menos algunos resultados.
        assert "No se ha encontrado resultado" not in self.driver.page_source

    def tearDown(self):
        # Cierra la ventana del navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

