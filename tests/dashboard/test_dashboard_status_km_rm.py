import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
class TestDashboardStatusKMRM:
    
    def test_status_km_belum_diisi(
        self,
        driver,
        login_as_user_belum_kuesioner
    ):
        dashboard = DashboardPage(driver)
        dashboard.open()
        dashboard.close_kuesioner_popup_if_present()

        print("KM TEXT =", dashboard.get_km_status_text())
        print("RM TEXT =", dashboard.get_rm_status_text())

        assert dashboard.is_km_not_filled()


    def test_status_rm_belum_diisi(
        self,
        driver,
        login_as_user_belum_kuesioner
    ):
        dashboard = DashboardPage(driver)
        dashboard.open()
        dashboard.close_kuesioner_popup_if_present()

        print("KM TEXT =", dashboard.get_km_status_text())
        print("RM TEXT =", dashboard.get_rm_status_text())

        assert dashboard.is_rm_not_filled()

    def test_status_km_sudah_isi_kuesioner(
            self,
            driver,
            login_as_user_sudah_kuesioner
    ):
        dashboard = DashboardPage(driver)
        assert dashboard.is_km_filled()
        print("KM TEXT =", dashboard.get_km_status_text_sudah_isi())

    
    def test_status_rm_sudah_isi_kuesioner(
            self,
            driver,
            login_as_user_sudah_kuesioner
    ):
        dashboard = DashboardPage(driver)
        assert dashboard.is_rm_filled()
        print("RM TEXT =", dashboard.get_rm_status_text_sudah_isi())

        