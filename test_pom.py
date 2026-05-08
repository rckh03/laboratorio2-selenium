from selenium import webdriver
from login_page import LoginPage, InventoryPage


def test_ejecucion_pom():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        # CASO 1: Login exitoso
        print("Ejecutando Caso 1...")
        login.login("standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 exitoso.")

        # CASO 2: Agregar al carrito
        print("Ejecutando Caso 2...")
        inventory.agregar_backpack()
        assert inventory.obtener_cantidad_carrito() == "1"
        print("✅ Caso 2 exitoso.")

        # CASO 3: Login fallido
        print("Ejecutando Caso 3...")
        driver.delete_all_cookies()
        login.login("locked_out_user", "secret_sauce")
        assert "locked out" in login.obtener_error()
        print("✅ Caso 3 exitoso.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()
        print("🔒 Navegador cerrado.")


test_ejecucion_pom()
