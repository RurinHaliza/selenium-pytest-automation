import pytest


class TestLoginPassword:

    VALID_EMAIL = "e41222052@student.polije.ac.id"
    VALID_PASSWORD = "e41222052@student.polije.ac.id"

    # ==========================
    # PASSWORD NEGATIVE CASES
    # ==========================

    def test_password_kosong(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password("")
        login_page.submit()

        assert login_page.has_html5_validation("password")

    def test_password_salah(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password("PasswordSalah123!")
        login_page.submit()

        assert login_page.is_login_failed()

    def test_password_hanya_spasi(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password("   ")
        login_page.submit()

        assert login_page.is_login_failed()

    def test_password_kurang_dari_8_karakter(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password("Abc1!")
        login_page.submit()

        assert login_page.is_login_failed()

    # ==========================
    # PASSWORD POSITIVE CASE
    # ==========================

    def test_password_valid(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password(self.VALID_PASSWORD)
        login_page.submit()

        assert login_page.is_login_success()
