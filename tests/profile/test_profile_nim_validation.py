import pytest
from datetime import datetime
from pages.profile_page import ProfilePage


class TestProfileNimValidation:

    # ======================================================
    # NIM VALIDATION
    # ======================================================

    def test_nim_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_nim = page.get_nim()
        page.set_nim("")
        page.click_save()
        assert page.get_nim() == default_nim

    def test_nim_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.set_nim("2022012345")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_nim() == "2022012345"

    def test_nim_bukan_angka(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_nim = page.get_nim
        page.set_nim("ABC12345")
        page.click_save()
        assert page.get_nim() == default_nim

    def test_nim_kurang_minimal(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_nim = page.get_nim
        page.set_nim("1234567")
        page.click_save()
        assert page.get_nim() == default_nim

    def test_nim_lebih_maksimal(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_nim = page.get_nim
        page.set_nim("1234567890123456")
        page.click_save()
        assert page.get_nim() == default_nim

