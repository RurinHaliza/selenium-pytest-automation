import os
import pytest
from pages.profile_page import ProfilePage


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")

class TestProfileUpload:

    def test_upload_jpg_berhasil(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Upload file JPG berhasil dan preview berubah
        """
        page.wait_until_page_loaded()

        old_src = page.get_profile_image_src()

        file_path = os.path.join(TEST_DATA_DIR, "Kucink_Jpg.jpg")
        page.upload_photo(file_path)
        page.click_save()
        page.refresh_page()

        new_src = page.get_profile_image_src()

        assert old_src != new_src


    def test_upload_png_berhasil(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Upload file PNG berhasil
        """
        old_src = page.get_profile_image_src()

        file_path = os.path.join(TEST_DATA_DIR, "Kucink_PNG.png")
        page.upload_photo(file_path)
        page.click_save()
        page.refresh_page()

        new_src = page.get_profile_image_src()

        assert old_src != new_src


    def test_upload_file_selain_gambar_ditolak(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
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


    def test_upload_file_lebih_800kb_ditolak(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Upload file > 800KB harus gagal
        """
        old_src = page.get_profile_image_src()

        file_path = os.path.join(TEST_DATA_DIR, "large_image.jpg")
        page.upload_photo(file_path)
        page.click_save()
        page.refresh_page()

        new_src = page.get_profile_image_src()

        assert old_src == new_src


    def test_preview_muncul_setelah_upload(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Preview image harus berubah sebelum save
        """
        old_src = page.get_profile_image_src()

        file_path = os.path.join(TEST_DATA_DIR, "Kucink_Jpg.jpg")
        page.upload_photo(file_path)

        new_src = page.get_profile_image_src()

        assert old_src != new_src


    def test_reset_mengembalikan_foto_default(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/profile")
        page = ProfilePage(driver)
        """
        Reset harus mengembalikan foto ke default
        """
        page.wait_until_page_loaded()

        page.click_reset_photo()
        page.refresh_page()

        src = page.get_profile_image_src()

        assert "defaultProfile" in src
