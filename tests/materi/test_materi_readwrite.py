import pytest
from pages.materi_readwrite_page import MateriReadWritePage
from selenium.webdriver.support import expected_conditions as EC

class TestMateriReadWrite:

    def test_readwrite_page_display_text_materi(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        text = page.get_text_materi()
        assert len(text) > 0

    def test_submit_rangkuman_success(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        rangkuman_valid = (
            "Enkapsulasi adalah konsep dalam pemrograman berorientasi objek "
            "yang digunakan untuk membungkus data dan method dalam satu kelas. "
            "Tujuannya adalah melindungi data agar tidak diakses langsung dari luar."
        )

        page.input_rangkuman(rangkuman_valid)
        page.submit_rangkuman()

        alert = page.success_message_displayed()
        assert "berhasil" in alert.text.lower()

    def test_submit_rangkuman_empty_should_fail(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        page.input_rangkuman("")
        page.submit_rangkuman()

        # tetap di halaman yang sama (validasi HTML required)
        assert "readwrite" in driver.current_url

    def test_submit_rangkuman_less_than_50_words_should_be_rejected(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        short_text = "Enkapsulasi adalah konsep OOP untuk melindungi data."
        page.input_rangkuman(short_text)
        page.submit_rangkuman()

        assert page.error_message_displayed()

    def test_submit_rangkuman_more_than_75_words_should_be_rejected(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        long_text = " ".join(["enkapsulasi"] * 80)
        page.input_rangkuman(long_text)
        page.submit_rangkuman()

        assert page.error_message_displayed()

    def test_input_rangkuman_textarea_displayed(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        textarea = page.wait.until(
            EC.visibility_of_element_located(page.RANGKUMAN_TEXTAREA)
        )

        assert textarea.is_displayed()
        assert textarea.is_enabled()

    def test_tugas_rangkuman_section_label_displayed(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        label = page.wait.until(
            EC.visibility_of_element_located(page.TUGAS_RANGKUMAN_LABEL)
        )

        assert label.is_displayed()
        assert "Tugas Rangkuman" in label.text

    def test_cannot_leave_page_without_submit_rangkuman(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        page.input_rangkuman("Rangkuman belum dikirim")
        page.go_to_visual()

        # Sistem HARUS menahan user di halaman ini
        assert "readwrite" in driver.current_url

    def test_textarea_cleared_after_submit(self, driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        page = MateriReadWritePage(driver)
        page.page_loaded()

        text = " ".join(["enkapsulasi"] * 50)
        page.input_rangkuman(text)
        page.submit_rangkuman()

        textarea = driver.find_element(*page.RANGKUMAN_TEXTAREA)
        assert textarea.get_attribute("value") == ""





