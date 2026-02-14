import pytest
from datetime import datetime
from pages.profile_page import ProfilePage


class TestProfileNamaValidation:

    # ======================================================
    # NAMA VALIDATION
    # ======================================================

    def test_nama_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("")
        page.click_save()
        assert page.get_nama_lengkap() == default_name

    def test_nama_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.set_nama_lengkap("Rurin Nurliza")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_nama_lengkap() == "Rurin Nurliza"

    def test_nama_kurang_5_karakter(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("Rin")
        page.click_save()
        assert page.get_nama_lengkap() == default_name, ("FAIL, Sistem tidak mengembalikan nama ke default")

    def test_nama_lebih_30_karakter(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("IniNamaYangSangatPanjangSekaliSeharusnyaTidakBoleh")
        page.click_save()
        assert page.get_nama_lengkap() == default_name, ("FAIL, Sistem tidak mengembalikan nama ke default")

    def test_nama_angka_semua(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("12345678")
        page.click_save()
        assert page.get_nama_lengkap() == default_name, ("FAIL, Sistem tidak mengembalikan nama ke default dan tidak memberika validasi error")

    def test_nama_simbol_semua(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("@@@@@@@")
        page.click_save()
        assert page.get_nama_lengkap() == default_name, ("FAIL, Sistem tidak mengembalikan nama ke default dan tidak memberika validasi error")



    