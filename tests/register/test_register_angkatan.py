import pytest
from datetime import datetime


@pytest.mark.usefixtures("driver")
class TestRegisterAngkatan:
    """
    RULE ANGKATAN:
    - Wajib diisi (HTML5)
    - Hanya angka
    - Minimal 2021
    - Maksimal tahun sekarang + 1
    """

    # =========================
    # NEGATIVE TEST CASES
    # =========================

    def test_angkatan_kosong(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = ""
        register_page.fill_form(valid_register_data)
        assert register_page.is_field_required("angkatan")

    def test_angkatan_hanya_spasi(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "   "
        register_page.fill_form(valid_register_data)
        assert register_page.is_field_required("angkatan")

    def test_angkatan_huruf(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "abcd"
        register_page.fill_form(valid_register_data)
        value = register_page.get_value("angkatan")
        assert value == ""

    def test_angkatan_simbol(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "@@@@"
        register_page.fill_form(valid_register_data)
        value = register_page.get_value("angkatan")
        assert value == ""

    def test_angkatan_kurang_dari_minimum(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "2019"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("angkatan")

    def test_angkatan_terlalu_besar(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "9999"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("angkatan")


    # =========================
    # POSITIVE TEST CASES
    # =========================

    def test_angkatan_valid_minimum(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = "2021"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_angkatan_valid_tahun_sekarang(self, register_page, valid_register_data):
        tahun_sekarang = str(datetime.now().year)
        valid_register_data["angkatan"] = tahun_sekarang
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_angkatan_valid_random(self, register_page, valid_register_data):
        valid_register_data["angkatan"] = valid_register_data["angkatan"]
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()
