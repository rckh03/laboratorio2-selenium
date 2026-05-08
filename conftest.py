import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_b64 = driver.get_screenshot_as_base64()
            img_html = (
                f'<div><img src="data:image/png;base64,{screenshot_b64}" '
                f'style="width:480px; border:2px solid red;" '
                f'onclick="window.open(this.src)"/></div>'
            )
            extras.append(pytest_html.extras.html(img_html))
    report.extra = extras
