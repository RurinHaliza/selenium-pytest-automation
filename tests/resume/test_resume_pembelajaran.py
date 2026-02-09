import pytest
from pages.resume_pembelajaran_page import ResumePembelajaranPage
from pages.materi_readwrite_page import MateriReadWritePage

class TestResumePembelajaran:

    def test_resume_empty_state_displayed(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/resume-pembelajaran")
        page = ResumePembelajaranPage(driver)
        page.page_loaded()

        assert page.is_empty_message_displayed() is True

    def test_resume_created_after_submit_rangkuman(self,driver, login_as_user_sudah_kuesioner):
        # 1. Kirim rangkuman dari Materi Read/Write
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/readwrite/1")
        materi_page = MateriReadWritePage(driver)
        materi_page.page_loaded()

        rangkuman_text = " ".join(["test resume"] * 50)
        materi_page.input_rangkuman(rangkuman_text)
        materi_page.submit_rangkuman()

        # 2. Buka Resume Pembelajaran
        driver.get(
            "https://hypermedialearning.sanggadewa.my.id/resume-pembelajaran"
        )

        resume_page = ResumePembelajaranPage(driver)
        resume_page.page_loaded()

        resume_content = resume_page.get_resume_text()
        assert rangkuman_text in resume_content

    def test_resume_persist_after_page_reload(self,driver, login_as_user_sudah_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/resume-pembelajaran")
        page = ResumePembelajaranPage(driver)
        page.page_loaded()

        first_load_text = page.get_resume_text()

        driver.refresh()
        page.page_loaded()

        second_load_text = page.get_resume_text()
        assert first_load_text == second_load_text




