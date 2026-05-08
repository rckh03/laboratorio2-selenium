from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración inicial
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


def ejecutar_pruebas():
    try:
        # --- CASO 1: Login Exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al Carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "1"
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login Fallido ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error
        print("✅ Caso 3 completado con éxito.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


ejecutar_pruebas()
