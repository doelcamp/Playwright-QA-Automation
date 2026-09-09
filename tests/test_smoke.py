from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_smoke_flujo_login_y_catalogo(page: Page):
    """SMOKE TEST: Validación de login y acceso a catálogo."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navegar()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_page.verificar_ingreso_exitoso()

    cantidad_productos = inventory_page.obtener_conteo_productos()
    assert cantidad_productos > 0, f"Error: Se esperaban productos pero se encontraron {cantidad_productos}"