import pytest
from pages.kuesioner_panduan_page import KuesionerPanduanPage


class TestKuesionerPanduan:

    def test_open_panduan_from_sidebar(self, driver, login_as_user_sudah_kuesioner):
        panduan = KuesionerPanduanPage(driver)
        panduan.open_from_sidebar()

        assert panduan.is_on_panduan_page()

    def test_click_mulai_kuesioner_redirect(self, driver, login_as_user_sudah_kuesioner):
        panduan = KuesionerPanduanPage(driver)
        panduan.open_from_sidebar()
        panduan.click_mulai_kuesioner()

        assert "kuesioner-ls" in driver.current_url

    def test_click_bantuan_redirect_whatsapp(self, driver, login_as_user_sudah_kuesioner):
        panduan = KuesionerPanduanPage(driver)
        panduan.open_from_sidebar()
        panduan.click_bantuan()

        current_url = driver.current_url

        assert "whatsapp.com" in current_url
        assert "6285290543351" in current_url

