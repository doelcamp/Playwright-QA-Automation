# Playwright QA Automation Framework

Este repositorio contiene un framework de automatización de pruebas de extremo a extremo (E2E) para entornos web, construido con un enfoque profesional, escalable y mantenible.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.14
* **Herramienta de Automatización:** Playwright
* **Framework de Pruebas:** Pytest
* **Reportes:** Pytest-HTML (Versión 4 con incrustación nativa de capturas en Base64 en caso de fallos)
* **Patrón de Diseño:** Page Object Model (POM)

## 📁 Estructura del Proyecto
* `pages/`: Clases que representan las páginas web y encapsulan los locators y acciones.
* `tests/`: Scripts de prueba que ejecutan los flujos de negocio y aserciones.
* `conftest.py`: Configuración global de accesorios (*fixtures*) y personalización de reportes HTML.

## 🚀 Instalación y Ejecución

1. Clonar el repositorio.
2. Crear y activar el entorno virtual (`venv`).
3. Instalar las dependencias y navegadores de Playwright:
   ```bash
   pip install playwright pytest pytest-html
   playwright install