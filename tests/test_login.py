import pytest
import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# ==========================================
# AQUÍ ABAJO YA PUEDEN IR TUS TESTS NORMALES
# ==========================================

# Test 1: Flujo funcional síncrono (¡Login funcional!)
def test_login_exitoso(page: Page):
    login = LoginPage(page)
    login.navegar("https://www.saucedemo.com/")
    login.iniciar_sesion("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# Test 2: Validación Visual (CONFIGURADO PARA FALLAR EN TU DEMO)
def test_diseño_visual_login(page: Page, extras): 
    login = LoginPage(page)
    
    # Navegamos a Playwright para que rompa contra el molde existente de Google
    login.navegar("https://playwright.dev/") 
    
    ruta_baseline = "login_page_baseline.png"
    
    if not os.path.exists(ruta_baseline):
        page.screenshot(path=ruta_baseline)
        pytest.skip("Baseline creado. Corre el test de nuevo.")
    
    ruta_actual = "login_page_actual.png"
    page.screenshot(path=ruta_actual)
    
    with open(ruta_baseline, "rb") as f1, open(ruta_actual, "rb") as f2:
        es_identico = f1.read() == f2.read()
        
    # Si no son idénticos, inyectamos la imagen usando el método de la lista de la v4
    if not es_identico:
        import base64
        import pytest_html
        
        bytes_pantalla = page.screenshot(type="png")
        encoded_string = base64.b64encode(bytes_pantalla).decode("utf-8")
        
        html_evidencia = f'''
        <div style="margin-top:10px; padding: 10px; background-color: #fdf7f7; border-left: 4px solid #d9534f;">
            <strong style="color:#d9534f;">📸 Evidencia del Fallo Visual Directo:</strong><br>
            <img src="data:image/png;base64,{encoded_string}" alt="Evidencia" style="width:450px; border:3px solid #d9534f; margin-top:5px;"/>
        </div>
        '''
        extras.append(pytest_html.extras.html(html_evidencia))

    assert es_identico, "¡Regresión Visual Detectada! La interfaz cambió respecto al molde original."

# Test 3: Validación de integridad de datos corporativos (Tablas/Catálogos)
def test_integridad_datos_productos(page: Page):
    login = LoginPage(page)
    login.navegar("https://www.saucedemo.com/")
    login.iniciar_sesion("standard_user", "secret_sauce")
    
    datos_en_pantalla = login.obtener_catalogo_productos()
    
    productos_esperados = {
        "Sauce Labs Backpack": "$29.99",
        "Sauce Labs Bike Light": "$9.99",
        "Sauce Labs Bolt T-Shirt": "$15.99",
        "Sauce Labs Fleece Jacket": "$49.99",
        "Sauce Labs Onesie": "$7.99",
        "Test.allTheThings() T-Shirt (Red)": "$15.99"
    }
    
    assert datos_en_pantalla == productos_esperados, "¡Error de integridad! Los datos de la interfaz cambiaron."