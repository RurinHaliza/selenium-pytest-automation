import pytest
import os
from pages.register_page import RegisterPage
from pages.live_coding_page import LiveCodingPage
from pages.profile_page import ProfilePage

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")

@pytest.mark.usefixtures("driver")
class TestRegression:

#Regression Daftar Akun
    def test_nama_valid_huruf_kecil(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "rurinhaliza"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_nim_valid_9_karakter(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E41222555"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_semester_valid_tengah(self, register_page, valid_register_data):
        valid_register_data["semester"] = "4"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_angkatan_valid_random(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = valid_register_data["angkatan"]
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_email_valid_student_polije(self, register_page, valid_register_data):
        valid_register_data["email"] = "siswa@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_password_valid(self, register_page, valid_register_data):
        """
        Password valid (huruf besar, kecil, angka, simbol)
        """
        valid_register_data["password"] = "Qwerty098"
        valid_register_data["konfirmasi_password"] = "Qwerty098"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_konfirmasi_password_sama(self, register_page, valid_register_data):
        valid_register_data["password"] = "Zxcvbn123"
        valid_register_data["konfirmasi_password"] = "Zxcvbn123"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

# Regression materi kinesthetic
    def test_submit_with_correct_code(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/materi/kinesthetic/1")
        page = LiveCodingPage(driver)

        page.append_code2("""
        Mahasiswa
        println
        """)
        page.submit_code()

        result = page.get_result_message()
        assert "Jawaban Benar" in result
        print(result)

    def test_next_button_on_first_page(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/materi/kinesthetic/1")
        page = LiveCodingPage(driver)
        initial_url = page.get_current_url()

        page.click_next()

        current_url = page.get_current_url()

        assert "/kinesthetic/2" in current_url 

#Regression Pofile
    def test_email_tampil_sesuai_akun(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        """
        Verifikasi email tampil sesuai akun dan tidak kosong
        """
        page.wait_until_page_loaded()

        email = page.get_email()

        assert email is not None
        #assert email != ""
        assert "@" in email
        assert email.endswith(".ac.id") 
        #or email.endswith(".com")

    def test_upload_file_selain_gambar_ditolak(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        """
        Upload file selain JPG/PNG harus ditolak
        """
        old_src = page.get_profile_image_src()

        file_path = os.path.join(TEST_DATA_DIR, "invalid_file.pdf")
        page.upload_photo(file_path)
        page.click_save()
        page.refresh_page()

        new_src = page.get_profile_image_src()

        assert old_src == new_src

    def test_nama_kosong(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        default_name = page.get_nama_lengkap()
        page.set_nama_lengkap("")
        page.click_save()
        assert page.get_nama_lengkap() == default_name

    def test_nim_kosong(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        default_nim = page.get_nim()
        page.set_nim("")
        page.click_save()
        assert page.get_nim() == default_nim

    def test_semester_valid(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        page.select_semester("1")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_semester() == "1"

    def test_angkatan_valid(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)

        page.select_angkatan("2025")
        page.click_save()
        page.wait_until_reload_after_save()

        assert page.get_selected_angkatan() == "2025"

    def test_button_simpan_update_data(self,driver,login_as_user_belum_kuesionerNew):
        driver.get("https://hypermedialearning.project2025.id/public/profile")
        page = ProfilePage(driver)
        new_name = "ItsTesting"
        page.set_nama_lengkap(new_name)
        page.click_save()
        page.wait_until_reload_after_save()
        assert page.get_nama_lengkap() == new_name
