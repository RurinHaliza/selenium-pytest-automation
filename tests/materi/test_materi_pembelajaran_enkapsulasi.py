import pytest
from pages.materi_pembelajaran_page import MateriPembelajaranPage


class TestMateriPembelajaranEnkapsulasi:

    def test_open_halaman_enkapsulasi(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()

        assert "/materi" in driver.current_url

    def test_tampilkan_learning_style_user(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()

        style = page.get_learning_style_user()
        assert style in ["Visual", "Auditory", "Read/Write", "Kinesthetic"]

    def test_mulai_belajar_learning_style_utama(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()
        page.click_mulai_belajar_utama()

        judul = page.get_judul_materi()
        assert judul != ""

    def test_pesan_materi_alternatif_muncul(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()

        assert page.wait.until(
            lambda d: d.find_element(*page.PESAN_ALTERNATIF)
        )

    def test_mulai_belajar_visual(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()
        page.click_visual()

        assert page.get_judul_materi() == "Materi Visual"

    def test_mulai_belajar_auditory(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()
        page.click_auditory()

        assert page.get_judul_materi() == "Materi Auditory"

    def test_mulai_belajar_read_write(self, driver, login_as_user_sudah_kuesioner):
        page = MateriPembelajaranPage(driver)
        page.open_from_sidebar()
        page.click_read_write()

        assert page.get_judul_materi() == "Materi Read / Write"
