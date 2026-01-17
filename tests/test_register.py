from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_register_valid_data(driver):
    """
    Test Scenario:
    Periksa sistem jika user mengisi seluruh form pendaftaran dengan data valid

    Technical Requirement:
    T1–T6, T7–T12, T13–T20, T21–T28, T29–T41

    Expected Result:
    Sistem menerima pendaftaran akun
    """

    register = RegisterPage(driver)
    register.open()

    # === DATA UNIK ===
    timestamp = int(time.time())
    email_unik = f"dummy_{timestamp}@polije.ac.id"
    nim_unik = f"E41{timestamp % 100000}"

    register.input_nama_lengkap("Budi Santoso")
    register.input_nim("E41234567")
    register.input_semester("6")
    register.input_angkatan("2022")
    register.input_email("dummy_test@polije.ac.id")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password1!")

    register.submit()

    # === WAIT PROSES SUBMIT ===
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != RegisterPage.URL
        or len(register.get_error_message()) > 0
    )

    # === ASSERTION ===
    assert "register" not in driver.current_url, \
        "Registrasi gagal, user masih berada di halaman register"

def test_register_nama_lengkap_kosong(driver):
    """
    Test Scenario:
    Nama Lengkap tidak diisi

    Technical Requirement:
    T1 – Nama Lengkap tidak boleh kosong

    Expected Result:
    Sistem menolak pendaftaran dan menampilkan validasi wajib isi
    """

    register = RegisterPage(driver)
    register.open()

    # Nama kosong
    register.input_nim("E41234567")
    register.input_semester("6")
    register.input_angkatan("2022")
    register.input_email("test@polije.ac.id")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password1!")

    register.submit()

    assert register.is_field_invalid(RegisterPage.NAMA_LENGKAP)
    assert "fill out" in register.get_validation_message(RegisterPage.NAMA_LENGKAP).lower()

def test_register_email_tidak_valid(driver):
    register = RegisterPage(driver)
    register.open()

    register.input_nama_lengkap("Budi Santoso")
    register.input_nim("E41234568")
    register.input_semester("6")
    register.input_angkatan("2022")
    register.input_email("email-salah-format")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password1!")

    register.submit()

    assert register.is_field_invalid(RegisterPage.EMAIL)

def test_register_password_tidak_sama(driver):
    register = RegisterPage(driver)
    register.open()

    register.input_nama_lengkap("Budi Santoso")
    register.input_nim("E41234569")
    register.input_semester("6")
    register.input_angkatan("2022")
    register.input_email("passwordbeda@polije.ac.id")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password2!")

    register.submit()

    errors = register.get_error_message()
    assert len(errors) > 0

def test_register_nim_kosong(driver):
    register = RegisterPage(driver)
    register.open()

    register.input_nama_lengkap("Budi Santoso")
    register.input_semester("6")
    register.input_angkatan("2022")
    register.input_email("nimkosong@polije.ac.id")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password1!")

    register.submit()

    assert register.is_field_invalid(RegisterPage.NIM)

def test_register_semester_bukan_angka(driver):
    register = RegisterPage(driver)
    register.open()

    register.input_nama_lengkap("Budi Santoso")
    register.input_nim("E41234570")
    register.input_semester("enam")
    register.input_angkatan("2022")
    register.input_email("semester@polije.ac.id")
    register.input_password("Password1!")
    register.input_konfirmasi_password("Password1!")

    register.submit()

    assert register.is_field_invalid(RegisterPage.SEMESTER)

def test_register_semua_field_kosong(driver):
    register = RegisterPage(driver)
    register.open()

    # ASSERTION TANPA CLICK
    assert register.is_field_invalid(RegisterPage.NAMA_LENGKAP)


