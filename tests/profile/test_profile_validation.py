import pytest
from datetime import datetime
from pages.profile_page import ProfilePage


class TestProfileValidation:

    # ======================================================
    # NAMA VALIDATION
    # ======================================================

    def test_nama_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nama_lengkap("")
        page.click_save()
        assert "tidak boleh kosong" in page.get_error_nama()

    def test_nama_kurang_5_karakter(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nama_lengkap("Rin")
        page.click_save()
        assert "minimal 5 karakter" in page.get_error_nama()

    def test_nama_lebih_30_karakter(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nama_lengkap("RinAndikaPutraWijayaSangatPanjangSekali")
        page.click_save()
        assert "maksimal 30 karakter" in page.get_error_nama()

    def test_nama_angka_semua(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nama_lengkap("12345678")
        page.click_save()
        assert "tidak valid" in page.get_error_nama()

    def test_nama_simbol_semua(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nama_lengkap("@@@@@@@")
        page.click_save()
        assert "tidak valid" in page.get_error_nama()

    def test_nama_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.set_nama_lengkap("Rin Andika")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_nama_lengkap() == "Rin Andika"

    # ======================================================
    # NIM VALIDATION
    # ======================================================

    def test_nim_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nim("")
        page.click_save()
        assert "tidak boleh kosong" in page.get_error_nim()

    def test_nim_bukan_angka(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nim("ABC12345")
        page.click_save()
        assert "harus berupa angka" in page.get_error_nim()

    def test_nim_kurang_minimal(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nim("1234567")
        page.click_save()
        assert "minimal" in page.get_error_nim()

    def test_nim_lebih_maksimal(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.set_nim("1234567890123456")
        page.click_save()
        assert "maksimal" in page.get_error_nim()

    def test_nim_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.set_nim("2022012345")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_nim() == "2022012345"

    # ======================================================
    # ANGKATAN VALIDATION
    # ======================================================

    def test_angkatan_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page = ProfilePage(driver)
        page.select_angkatan("")
        page.click_save()
        assert "tidak boleh kosong" in page.get_error_angkatan()

    def test_angkatan_huruf(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_angkatan("abcd")
        page.click_save()
        assert "tidak valid" in page.get_error_angkatan()

    def test_angkatan_kurang_2000(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_angkatan("1999")
        page.click_save()
        assert "tidak valid" in page.get_error_angkatan()

    def test_angkatan_lebih_tahun_sekarang(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        next_year = str(datetime.now().year + 1)
        page.select_angkatan(next_year)
        page.click_save()
        assert "tidak valid" in page.get_error_angkatan()

    def test_angkatan_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)

        page.select_angkatan("2022")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_angkatan() == "2022"

    # ======================================================
    # SEMESTER VALIDATION
    # ======================================================

    def test_semester_kosong(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("")
        page.click_save()
        assert "tidak boleh kosong" in page.get_error_semester()

    def test_semester_bukan_angka(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("abc")
        page.click_save()
        assert "tidak valid" in page.get_error_semester()

    def test_semester_kurang_1(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("0")
        page.click_save()
        assert "tidak valid" in page.get_error_semester()

    def test_semester_lebih_14(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("20")
        page.click_save()
        assert "tidak valid" in page.get_error_semester()

    def test_semester_valid(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        page.select_semester("5")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_semester() == "5"
