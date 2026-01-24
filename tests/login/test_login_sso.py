import pytest

class TestLoginSSOGoogle:

    def test_button_sso_google_tersedia(self, login_page):
        assert login_page.driver.find_element(
            *login_page.SSO_GOOGLE_BUTTON
        )

    def test_redirect_ke_google_oauth(self, login_page):
        login_page.click_sso_google()

        assert login_page.is_redirected_to_google()
