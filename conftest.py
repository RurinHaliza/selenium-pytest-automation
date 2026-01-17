import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.register_page import RegisterPage
from utils.data_generator import generate_valid_register_data


# ===============================
# FIXTURE DRIVER
# ===============================
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


# ===============================
# FIXTURE REGISTER PAGE
# ===============================
@pytest.fixture
def register_page(driver):
    page = RegisterPage(driver)
    page.open()
    return page


# ===============================
# DATA REGISTER VALID (FINAL)
# ===============================
@pytest.fixture
def valid_register_data():
    """
    - Data selalu VALID
    - Data SELALU BARU setiap test
    - Field boleh dioverride di test
    """
    data = generate_valid_register_data()

    # pastikan field WAJIB selalu ada
    data.setdefault("nama_lengkap", data["nama"])
    data.setdefault("konfirmasi_password", data["password"])

    return data


# ===============================
# SCREENSHOT SAAT FAIL
# ===============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Ambil screenshot otomatis jika test FAIL
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(file_path)
            print(f"\n📸 Screenshot saved: {file_path}")
