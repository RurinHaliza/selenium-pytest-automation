import pytest


@pytest.mark.usefixtures("driver")
class TestRegisterNIM:
    """
    RULE FINAL NIM:
    - Tidak boleh kosong (HTML5 required)
    - Tidak boleh spasi
    - Harus kombinasi huruf + angka
    - Tidak boleh karakter khusus
    - Minimal 9 karakter
    - Maksimal 10 karakter
    """

    # =========================
    # REQUIRED (HTML5)
    # =========================

    def test_nim_kosong(self, register_page, valid_register_data):
        valid_register_data["nim"] = ""
        register_page.fill_form(valid_register_data)

        # ❌ JANGAN submit
        assert register_page.is_field_required("NIM")

    # =========================
    # NEGATIVE (SERVER / JS)
    # =========================

    def test_nim_spasi_saja(self, register_page, valid_register_data):
        valid_register_data["nim"] = "     "
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_mengandung_spasi(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E 4122987"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_hanya_angka(self, register_page, valid_register_data):
        valid_register_data["nim"] = "412227890"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_hanya_huruf(self, register_page, valid_register_data):
        valid_register_data["nim"] = "ABCDEFGHI"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_karakter_khusus(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E41222@89"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_kurang_dari_9_karakter(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E41222"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    def test_nim_lebih_dari_10_karakter(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E41222789099"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("NIM")

    # =========================
    # POSITIVE
    # =========================

    def test_nim_valid_9_karakter(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E41222789"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()

    def test_nim_valid_10_karakter(self, register_page, valid_register_data):
        valid_register_data["nim"] = "E412227890"
        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()
