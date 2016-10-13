__author__ = 'hola'

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BuscoAyudaTest(unittest.TestCase):
    """docstring for ."""
    def setUp(self):
        self.browser = webdriver.Firefox()

    def  tearDown(self):
        #self.browser.quit()
        pass

    def test_title(self):
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get("http://127.0.0.1:8000")

        register = self.browser.find_element_by_id('id_register')
        register.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Fulano')

        apellido = self.browser.find_element_by_id('id_apellidos')
        apellido.send_keys('Perez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('2')

        self.browser.find_element_by_xpath('//select[@id=\'id_tiposDeServicio\']/option[text()=\'Desarrollador Web\']').click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('37465827475')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('qwe@qwe.qwe')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\\Users\\alejo\\Google Drive\\IFTTT\\Spotify\\Orochi by Orochi.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('NoEsOtroFulano')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        boton_grabar = self.browser.find_element_by_id('id_grabar')
        boton_grabar.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[contains(text(), "Fulano Perez")]')
        self.assertIn('Fulano Perez', span.text)

    def test_ver_detalle(self):
        self.browser.get("http://127.0.0.1:8000")
        span = self.browser.find_element(By.XPATH, '//span[contains(text(), "Fulano Perez")]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[contains(text(), "Fulano Perez")]')
        self.assertIn('Fulano Perez', h2.text)


if __name__ == '__main__':
    unittest.main()
