import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    import os

    if os.environ.get("CI"):  # solo en GitHub Actions
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Toma screenshot automático si un test falla y lo incrusta en el reporte."""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_b64 = driver.get_screenshot_as_base64()
            img_html = (
                f"<div>"
                f'<img src="data:image/png;base64,{screenshot_b64}" '
                f'style="width:480px; border:2px solid red; cursor:pointer;" '
                f'onclick="window.open(this.src)" '
                f'title="Clic para ampliar"/>'
                f"</div>"
            )
            extras.append(pytest_html.extras.html(img_html))

    report.extra = extras
