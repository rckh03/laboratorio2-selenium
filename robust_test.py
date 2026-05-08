from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)  # espera máximo 10 segundos por elemento

try:
    # --- CASO 1: Login con espera explícita ---
    print("Ejecutando Caso 1: Login seguro...")
    driver.get("https://www.saucedemo.com")

    # Espera a que el campo sea VISIBLE antes de escribir
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
        "standard_user"
    )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))
    print("✅ Caso 1 exitoso.")

    # --- CASO 2: Agregar al carrito esperando que el botón sea clicable ---
    print("Ejecutando Caso 2: Agregar producto...")

    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    badge = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    print(f"✅ Caso 2 exitoso. Carrito tiene {badge.text} producto(s).")

    # --- CASO 3: Validar mensaje de error ---
    print("Ejecutando Caso 3: Login fallido...")
    driver.delete_all_cookies()
    driver.get("https://www.saucedemo.com")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
        "locked_out_user"
    )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    print(f"✅ Caso 3 exitoso. Mensaje: '{error.text}'")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    print("🔒 Navegador cerrado.")
