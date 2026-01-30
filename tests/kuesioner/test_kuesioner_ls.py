import pytest
from pages.kuesioner_ls_page import KuesionerLSPage

class TestKuesionerLS:

    def test_open_kuesioner_ls(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerLSPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()

        assert "kuesioner-ls" in driver.current_url

    def test_submit_without_answer_should_fail(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerLSPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()

        # jawab hanya 15 dari 16
        for i in range(1, 16):
            page.answer_question(i)

        page.submit()

        assert "kuesioner-ls" in driver.current_url

    def test_submit_success_redirect_to_mai(self, driver, login_as_user_belum_kuesioner):
        page = KuesionerLSPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()

        page.answer_all_questions()
        page.submit()

        assert "kuesioner-mai" in driver.current_url

    def test_force_navigation_before_submit_allowed_known_issue(
        self, driver, login_as_user_belum_kuesioner
    ):
        page = KuesionerLSPage(driver)
        page.open_from_sidebar()
        page.click_mulai_kuesioner()

        # jawab sebagian (belum selesai)
        page.answer_question(1)
        page.answer_question(2)

        # user paksa pindah halaman
        page.force_navigate_to_dashboard()

        # EXPECTED (KNOWN ISSUE):
        # sistem langsung pindah tanpa validasi
        assert "dashboard" in driver.current_url
