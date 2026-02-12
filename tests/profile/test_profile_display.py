import pytest
from pages.profile_page import ProfilePage

class TestProfileDisplay:

    def test_email_tampil_sesuai_akun(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Verifikasi email tampil sesuai akun dan tidak kosong
        """
        page.wait_until_page_loaded()

        email = page.get_email()

        assert email is not None
        assert email != ""
        assert "@" in email
        assert email.endswith(".ac.id") 
        #or email.endswith(".com")


    def test_email_tidak_bisa_diedit(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Verifikasi email memiliki attribute readonly
        """
        assert page.is_email_readonly() is True


    def test_nim_tampil_sesuai_akun(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Verifikasi NIM tampil dan tidak kosong
        """
        nim = page.get_nim()

        assert nim is not None
        assert nim != ""
        assert len(nim) >= 9
        assert len(nim) <= 10


    def test_semester_tampil_sesuai_akun(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Verifikasi semester memiliki selected value
        """
        semester = page.get_selected_semester()

        assert semester is not None
        assert semester.isdigit()
        assert int(semester) >= 1
        assert int(semester) <= 8


    def test_angkatan_tampil_sesuai_akun(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Verifikasi angkatan memiliki selected value
        """
        angkatan = page.get_selected_angkatan()

        assert angkatan is not None
        assert angkatan.isdigit()
        assert len(angkatan) == 4
