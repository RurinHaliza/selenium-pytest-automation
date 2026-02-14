import pytest
from pages.logout_page import LogoutPage


# ===============================
# 1️⃣ Test: Modal Muncul
# ===============================

class TestLogout:

    def test_logout_modal_muncul(self, driver, login_as_user_sudah_kuesioner):
        logout = LogoutPage(driver)

        logout.open_user_dropdown()
        logout.click_logout_menu()

        assert logout.is_logout_modal_visible()


    # ===============================
    # 2️⃣ Test: Klik Tidak → Tetap di halaman
    # ===============================
    def test_logout_tidak_tetap_di_dashboard(self, driver, login_as_user_sudah_kuesioner):
        logout = LogoutPage(driver)

        current_url = driver.current_url

        logout.open_user_dropdown()
        logout.click_logout_menu()
        logout.click_tidak()

        assert driver.current_url == current_url


    # ===============================
    # 3️⃣ Test: Klik Ya → Redirect ke Home
    # ===============================
    def test_logout_ya_redirect_ke_home(self, driver, login_as_user_sudah_kuesioner):
        logout = LogoutPage(driver)

        logout.open_user_dropdown()
        logout.click_logout_menu()
        logout.click_ya_logout()

        logout.wait_until_redirect_to_home()

        assert "dashboard" not in driver.current_url.lower()
