import pytest
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("driver")
class TestRegisterNamaLengkap:
    """
    RULE FINAL NAMA LENGKAP:
    - Minimal 5 karakter
    - Maksimal 30 karakter
    - HANYA boleh huruf dan spasi
    - Huruf kapital/kecil bebas
    - TIDAK BOLEH angka atau simbol
    """

    # =========================
    # NEGATIVE TEST CASES
    # =========================

    def test_nama_kosong(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = ""
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_field_required("nama_lengkap")

    def test_nama_hanya_spasi(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "     "
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_kurang_dari_5_karakter(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "Aa"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_lebih_dari_30_karakter(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "B" * 31
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_angka_semua(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "98076545"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_simbol_semua(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "######"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_huruf_dan_angka(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "Bagus123"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    def test_nama_huruf_dan_simbol(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "Gilang@Putra"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Nama Lengkap")

    # =========================
    # POSITIVE TEST CASES
    # =========================

    def test_nama_valid_huruf_kecil(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "gilang bagus"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_nama_valid_huruf_kapital(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "GILANG RAMADAN"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_nama_valid_huruf_dan_spasi(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "Gilang Rama"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_nama_valid_minimal_karakter(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "Gilang B"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_nama_valid_maksimal_karakter(self, register_page, valid_register_data):
        valid_register_data["nama_lengkap"] = "C" * 30
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()
