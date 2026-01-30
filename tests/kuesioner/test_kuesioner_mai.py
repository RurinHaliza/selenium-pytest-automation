import pytest
from pages.kuesioner_mai_page import KuesionerMAIPage

class TestKuesionerMAI:

    def test_open_kuesioner_mai(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerMAIPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()
        page.answer_all_questions()
        page.submit()

        assert "kuesioner-mai" in driver.current_url

    def test_submit_mai_without_answer_should_fail(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerMAIPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()
        page.answer_all_questions()
        page.submit()

        page.submit()

        # tetap di halaman MAI
        assert "kuesioner-mai" in driver.current_url

    def test_submit_mai_success_redirect_to_history(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerMAIPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()
        page.answer_all_questions()
        page.submit()

        page.answer_all_questions()
        page.submit()

        assert "history-kuesioner" in driver.current_url
