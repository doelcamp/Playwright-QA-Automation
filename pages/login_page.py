from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def navegar(self, url="https://www.saucedemo.com/"):
        """Navega a la URL base de la aplicación."""
        self.page.goto(url)

    def iniciar_sesion(self, usuario: str, contrasenia: str):
        """Llena credenciales y hace clic en el botón de login."""
        self.username_input.fill(usuario)
        self.password_input.fill(contrasenia)
        self.login_button.click()