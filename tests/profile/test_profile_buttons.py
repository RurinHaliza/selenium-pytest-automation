import pytest
from pages.profile_page import ProfilePage

class TestProfileButton:

    def test_button_simpan_update_data(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        new_name = "Ini Testing"
        page.set_nama_lengkap(new_name)
        page.click_save()
        page.wait_until_reload_after_save()
        assert page.get_nama_lengkap() == new_name


    def test_button_simpan_validasi_gagal_revert(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("")
        page.click_save()
        assert page.get_nama_lengkap() == default_name


    def test_button_batal_kembali_ke_default(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("Nama Tidak Disimpan")
        page.click_cancel()
        assert page.get_nama_lengkap() == default_name
