from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Localizadores utilizando atributos orientados a testing (mejores prácticas)
        self.title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.inventory_items = page.locator(".inventory_item")

    def verificar_ingreso_exitoso(self):
        """Valida que el título 'Products' sea visible en la interfaz."""
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Products")

    def obtener_conteo_productos(self) -> int:
        """Devuelve la cantidad de productos visibles en el catálogo."""
        return self.inventory_items.count()