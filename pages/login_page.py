# Cambiamos async_api por sync_api
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def navegar(self, url: str):
        self.page.goto(url)

    def iniciar_sesion(self, usuario: str, contrasenia: str):
        self.username_input.fill(usuario)
        self.password_input.fill(contrasenia)
        self.login_button.click()

    def obtener_catalogo_productos(self) -> dict:
        """Extrae los nombres y precios de los productos de la interfaz y los devuelve como un diccionario."""
        # Localizamos todos los contenedores de productos en la página
        items = self.page.query_selector_all(".inventory_item")
        catalogo = {}
        
        for item in items:
            # Extraemos el texto del nombre y del precio para cada elemento
            nombre = item.query_selector(".inventory_item_name").inner_text()
            precio = item.query_selector(".inventory_item_price").inner_text()
            # Guardamos en el diccionario: {'Nombre Producto': '$Precio'}
            catalogo[nombre] = precio
            
        return catalogo
        