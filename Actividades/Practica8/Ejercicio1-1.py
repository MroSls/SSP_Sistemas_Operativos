from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

# Ruta al ejecutable de Microsoft Edge WebDriver
ruta_driver = r"..\SSP SISTEMAS OPERATIVOS\clase\msedgedriver.exe"

# URL del formulario
url_formulario = "https://forms.office.com/Pages/ResponsePage.aspx?id=_eeS24nuHUm_P6918HPgz8kGucio5uRAucnQjmvXLKJUNURCSlVMNDg4RTBQRk9JNkhYMEFSUFJMOS4u"

# Diccionario con los datos para completar el formulario
datos_formulario = {
    "Nombre": "Tu nombre",
    "Apellido": "Tu apellido",
    "Correo electrónico": "tucorreo@email.com",
    "Mensaje": "Este es un mensaje de prueba."
}

# Iniciar el servicio de WebDriver y crear una instancia del navegador
servicio = Service(executable_path=ruta_driver)
driver = webdriver.Edge(service=servicio)

# Acceder al formulario
driver.get(url_formulario)

# Completar los campos del formulario    
for nombre_campo, valor_campo in datos_formulario.items():
    campo = driver.find_element(By.NAME, nombre_campo)
    campo.send_keys(valor_campo)

# Enviar el formulario
boton_enviar = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#boton_enviar.click()

# Cerrar el navegador
driver.quit()
