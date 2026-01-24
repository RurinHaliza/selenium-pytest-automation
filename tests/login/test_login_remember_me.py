import pytest

@pytest.mark.usefixtures("driver")
class TestLoginRememberMe:

    VALID_EMAIL = "e41222052@student.polije.ac.id"
    VALID_PASSWORD = "e41222052@student.polije.ac.id"

    def test_remember_me_checkbox_dapat_dicentang(self, login_page):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password(self.VALID_PASSWORD)
        login_page.click_remember_me()

        assert login_page.is_remember_me_checked()

    def test_login_dengan_remember_me_dan_refresh(self, login_page, driver):
        login_page.fill_email(self.VALID_EMAIL)
        login_page.fill_password(self.VALID_PASSWORD)
        login_page.click_remember_me()
        login_page.submit()

        assert login_page.is_login_success()

        # refresh halaman
        driver.refresh()

        # masih di dashboard
        assert login_page.is_login_success()
