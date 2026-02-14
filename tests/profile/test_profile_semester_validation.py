import pytest
from datetime import datetime
from pages.profile_page import ProfilePage


class TestProfileSemesterValidation:

    # ======================================================
    # SEMESTER VALIDATION
    # ======================================================

    def test_semester_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("5")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_semester() == "5"

    def test_semester_dropdown_options(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        options = page.get_all_semester_options()

        assert options == ["1", "2", "3", "4", "5", "6", "7", "8"]

    
