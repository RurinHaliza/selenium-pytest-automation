import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.register_page import RegisterPage
from utils.data_generator import generate_valid_register_data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


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


# ===============================
# FIXTURE LOGIN PAGE
# ===============================
@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

# =========================
# LOGIN FIXTURES FOR TEST DASHBOARD
# =========================

@pytest.fixture
def login_as_user_belum_kuesioner(driver):
    """
    User valid, BELUM pernah mengisi kuesioner
    Digunakan untuk:
    - popup dashboard
    - status KM / RM kosong
    """

    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_email("e41222052@student.polije.ac.id")
    login_page.fill_password("e41222052@student.polije.ac.id")
    login_page.submit()

    dashboard = DashboardPage(driver)
    dashboard.open()

    return driver


@pytest.fixture
def login_as_user_sudah_kuesioner(driver):
    """
    User valid, SUDAH pernah mengisi kuesioner
    Digunakan untuk:
    - status KM / RM tersedia
    - tidak ada popup
    """

    login_page = LoginPage(driver)
    login_page.open()

    # Akun yang SUDAH isi kuesioner
    login_page.fill_email("tester@polije.ac.id")
    login_page.fill_password("tester@polije.ac.id")
    login_page.submit()

    dashboard = DashboardPage(driver)
    dashboard.open()

    return driver

