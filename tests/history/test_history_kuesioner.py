import re
import pytest
from pages.history_kuesioner_page import HistoryKuesionerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login_as_user_belum_kuesioner")
class TestHistoryKuesioner:

    def test_history_page_loaded(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()
        assert page.is_page_loaded()

    def test_km_dan_rm_value(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        assert page.get_km_value() in ["low", "medium", "high"]
        assert page.get_rm_value() in ["low", "medium", "high"]

    def test_ringkasan_skor_gaya_belajar(self, driver):
        """
        PASSED berarti:
        - 4 gaya belajar muncul
        - Label sesuai requirement
        - Nilai skor valid (angka)
        """
        page = HistoryKuesionerPage(driver)
        page.open()

        scores = page.get_scores()

        expected_labels = {"Visual", "Auditory", "Read/Write", "Kinesthetic"}

        assert set(scores.keys()) == expected_labels, (
            f"Label tidak sesuai: {scores.keys()}"
        )

        for label, value in scores.items():
            assert value.isdigit(), f"Skor {label} bukan angka: {value}"

    def test_progress_pengisian_100_persen(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        progress = page.get_progress_value()
        assert progress == "100", f"Progress seharusnya 100%, tetapi {progress}%"

    def test_gaya_belajar_dominan_valid(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        dominant = page.get_dominant_style()
        assert dominant in ["Visual", "Auditory", "Read/Write", "Kinesthetic"], (
            f"Gaya dominan tidak valid: {dominant}"
        )

    def test_button_mulai_belajar_redirect(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        page.click_mulai()

        WebDriverWait(driver, 10).until(
            lambda d: "materi" in d.current_url
        )

        assert "materi" in driver.current_url


    def test_tabel_riwayat_memuat_data(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        rows = page.get_history_rows()
        assert len(rows) > 0, "Tabel riwayat kosong"

    def test_format_tanggal_valid(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        row_text = page.get_history_rows()[0].text
        assert re.search(r"\d{2}\s[A-Za-z]{3}\s\d{4}", row_text), (
            f"Format tanggal tidak valid: {row_text}"
        )

    def test_button_ubah_redirect(self, driver):
        page = HistoryKuesionerPage(driver)
        page.open()

        page.click_ubah()
        WebDriverWait(driver, 5).until(EC.url_contains("kuesioner"))
        assert "kuesioner" in driver.current_url

    def test_button_unduh_redirect(self, driver):
        """
        PASSED berarti:
        - Tombol bisa diklik
        - Redirect ke halaman user-result berhasil
        """
        page = HistoryKuesionerPage(driver)
        page.open()

        page.click_unduh()

        WebDriverWait(driver, 5).until(EC.url_contains("user-result"))
        assert "user-result" in driver.current_url