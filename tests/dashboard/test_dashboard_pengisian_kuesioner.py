import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.dashboard
class TestDashboardPengisianKuesioner:

    def test_section_pengisian_kuesioner_tampil(self, driver, login_as_user_sudah_kuesioner):
        dashboard = DashboardPage(driver)
        dashboard.open()

        assert dashboard.is_pengisian_kuesioner_section_visible()

    def test_kuesioner_vark_mai_tampil(self, driver, login_as_user_sudah_kuesioner):
        dashboard = DashboardPage(driver)
        dashboard.open()

        assert dashboard.is_kuesioner_vark_mai_visible()

    def test_click_isi_kuesioner_redirect(self, driver, login_as_user_sudah_kuesioner):
        dashboard = DashboardPage(driver)
        dashboard.open()

        dashboard.click_isi_kuesioner()

        assert "kuesioner" in driver.current_url
