import pytest
from pages.live_coding_page import LiveCodingPage

class TestKinesthetic:

    def test_live_coding_page_loaded(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)

        assert page.is_page_loaded()
        assert page.editor_is_visible()
        assert "Hasil Output" in page.get_expected_output_text()

    def test_submit_without_completing_code(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)

        page.submit_code()
        result = page.get_result_message()

        assert "Jawaban Salah" in result
        assert "Seharusnya" in result

    def test_submit_with_wrong_code(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)

        page.append_code("System.out.println(\"SALAH\");")
        page.submit_code()

        result = page.get_result_message()
        assert "Jawaban Salah" in result
        assert "Seharusnya" in result

    def test_submit_with_correct_code(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)

        page.append_code(
        "System.out.println(m1.getNama() + \" | IPK: \" + m1.getIpk() + \"\\n\" + m2.getNama() + \" | IPK: \" + m2.getIpk());")
        page.submit_code()

        result = page.get_result_message()
        assert "Jawaban Benar" in result

    def test_default_code_is_displayed(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)
        code = page.get_editor_value()

        assert code.strip() != "", \
            "FAIL: Kode bawaan materi tidak tampil pada editor"
        
    def test_popup_can_be_closed(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)
        page.append_code("\nprint('test')")
        page.submit_code()

        page.wait_popup_visible()
        assert page.is_popup_visible()

        page.close_result_modal()

        assert not page.is_popup_visible(), \
            "FAIL: Popup evaluasi tidak tertutup"
        
    def test_previous_button_on_first_page(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)
        initial_url = page.get_current_url()

        page.click_previous()

        current_url = page.get_current_url()

        assert current_url == initial_url, (
            "FAIL: Tombol Sebelumnya pada halaman pertama "
            "seharusnya tidak berpindah halaman"
        )

        assert not page.is_404_page(), (
            "FAIL: Tombol Sebelumnya menyebabkan halaman 404"
        )

    def test_next_button_on_first_page(self,driver,login_as_user_belum_kuesioner):
        driver.get("https://hypermedialearning.sanggadewa.my.id/materi/kinesthetic/1")
        page = LiveCodingPage(driver)
        initial_url = page.get_current_url()

        page.click_next()

        current_url = page.get_current_url()

        assert current_url != initial_url, (
            "FAIL: Tombol Selanjutnya tidak berpindah ke halaman berikutnya"
        )

        assert not page.is_404_page(), (
            "FAIL: Tombol Selanjutnya menyebabkan halaman 404"
        )




