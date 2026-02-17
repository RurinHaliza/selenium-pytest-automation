import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
class TestDashboardPopup:

    def test_popup_muncul_jika_belum_isi_kuesioner(self, driver, login_as_user_belum_kuesioner2):
        dashboard = DashboardPage(driver)
        dashboard.open()

        assert dashboard.is_popup_visible()

    def test_button_isi_kuesioner_redirect(self, driver, login_as_user_belum_kuesioner2):
        dashboard = DashboardPage(driver)
        dashboard.open()

        dashboard.click_isi_kuesioner_pop_up()

        assert dashboard.is_redirected_to_kuesioner()

    def test_button_close_x_menutup_popup(self, driver, login_as_user_belum_kuesioner2):
        dashboard = DashboardPage(driver)
        dashboard.open()

        dashboard.close_popup_with_x()
        dashboard.wait_popup_disappear()

        assert not dashboard.is_popup_visible()
