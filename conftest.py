import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Buscamos si el test tiene acceso a la sesión del navegador ('page')
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            import pytest_html
            
            # Tomamos la captura de pantalla directamente en memoria (Base64) 
            # ¡Sin depender de archivos en el disco!
            screenshot_base64 = page.screenshot(type="png").hex()
            # Convertimos los bytes a formato base64 correcto
            import base64
            bytes_simulados = page.screenshot(type="png")
            encoded_string = base64.b64encode(bytes_simulados).decode("utf-8")
            
            # Formateamos el bloque HTML estructurado
            html = f'''
            <div style="margin-top: 15px; padding: 10px; border-left: 4px solid #d9534f; background-color: #fdf7f7;">
                <strong style="color:#d9534f; font-size: 14px;">📸 Evidencia del Fallo Visual Directo:</strong><br>
                <img src="data:image/png;base64,{encoded_string}" alt="Evidencia" style="width:500px; border:2px solid #d9534f; margin-top:10px; cursor:pointer;" onclick="window.open(this.src)"/>
            </div>
            '''
            extra.append(pytest_html.extras.html(html))
            report.extra = extra