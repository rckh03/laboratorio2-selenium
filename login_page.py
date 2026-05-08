from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Selectores centralizados aquí
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def abrir(self):
        self.driver.get("https://www.saucedemo.com")

    def ingresar_credenciales(self, usuario, password):
        self.wait.until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text

    def login(self, usuario, password):
        self.abrir()
        self.ingresar_credenciales(usuario, password)
        self.click_login()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def agregar_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

    def obtener_cantidad_carrito(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
