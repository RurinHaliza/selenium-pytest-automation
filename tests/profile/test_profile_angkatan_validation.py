import pytest
from datetime import datetime
from pages.profile_page import ProfilePage

   
    # ======================================================
    # ANGKATAN VALIDATION
    # ======================================================

class TestProfileAngkatanValidation:

    def test_angkatan_dropdown_options(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        current_year = datetime.now().year

        expected_years = [
            str(current_year - i) for i in reversed(range(7))
        ]

        actual_years = page.get_all_angkatan_options()

        assert actual_years == expected_years

    def test_angkatan_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.select_angkatan("2022")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_angkatan() == "2022"