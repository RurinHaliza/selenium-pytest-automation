import pytest


@pytest.mark.usefixtures("driver")
class TestLoginEmail:
    """
    TEST LOGIN - EMAIL FIELD
    """

    VALID_EMAIL = "e41222052@student.polije.ac.id"
    VALID_PASSWORD = "e41222052@student.polije.ac.id"

    # =========================
    # POSITIVE TEST
    # =========================

    def test_login_email_valid(self, login_page):
        login_page.open()
        login_page.login(
            self.VALID_EMAIL,
            self.VALID_PASSWORD
        )

        assert login_page.is_login_success()

    # =========================
    # NEGATIVE TESTS
    # =========================

    def test_login_email_salah_password_benar(self, login_page):
        login_page.open()
        login_page.login(
            "salah@student.polije.ac.id",
            self.VALID_PASSWORD
        )

        assert login_page.has_global_error()

    def test_login_email_kosong(self, login_page):
        login_page.open()
        login_page.fill_email("")
        login_page.fill_password(self.VALID_PASSWORD)
        login_page.click_login()

        assert login_page.is_field_required("email")

    def test_login_email_tanpa_at(self, login_page):
        login_page.open()
        login_page.login(
            "e41222052student.polije.ac.id",
            self.VALID_PASSWORD
        )

        assert login_page.get_email_validation_message()

    def test_login_email_hanya_spasi(self, login_page):
        login_page.open()
        login_page.login(
            "   ",
            self.VALID_PASSWORD
        )

        assert login_page.get_email_validation_message()

    def test_login_email_tidak_terdaftar(self, login_page):
        login_page.open()
        login_page.login(
            "tidakterdaftar@student.polije.ac.id",
            self.VALID_PASSWORD
        )

        assert login_page.has_global_error()
