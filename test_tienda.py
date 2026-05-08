import pytest
from selenium import webdriver
from login_page import LoginPage, InventoryPage

# ← Ya NO hay fixture driver aquí, lo hereda de conftest.py


def test_login_exitoso(driver):
    """Caso 01 - Login con credenciales válidas."""
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_agregar_al_carrito(driver):
    """Caso 02 - Agregar producto al carrito."""
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.login("standard_user", "secret_sauce")
    inventory.agregar_backpack()
    assert inventory.obtener_cantidad_carrito() == "1"


def test_login_fallido(driver):
    """Caso 03 - Usuario bloqueado ve mensaje de error."""
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.obtener_error()
