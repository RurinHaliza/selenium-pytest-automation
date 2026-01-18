import pytest


@pytest.mark.usefixtures("driver")
class TestRegisterKonfirmasiPassword:
    """
    RULE KONFIRMASI PASSWORD:
    - Wajib diisi
    - Harus sama dengan password
    - Validasi muncul setelah klik submit
    """

    # =========================
    # NEGATIVE TEST CASES
    # =========================

    def test_konfirmasi_password_kosong(self, register_page, valid_register_data):
        """
        Konfirmasi password kosong → HTML5 required
        """
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = ""

        register_page.fill_form(valid_register_data)

        assert register_page.is_field_required("konfirmasi_password")

    def test_konfirmasi_password_hanya_spasi(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "   "

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_konfirmasi_password_tidak_sama(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "Abcdef2@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_konfirmasi_password_lebih_pendek(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "Abcdef1"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_konfirmasi_password_lebih_panjang(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "Abcdef1@xxx"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    # =========================
    # POSITIVE TEST CASES
    # =========================

    def test_konfirmasi_password_sama(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "Abcdef1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()

    def test_konfirmasi_password_valid_dengan_spasi(self, register_page, valid_register_data):
        """
        Jika password mengandung spasi dan konfirmasi sama → valid
        """
        valid_register_data["password"] = "Abc def1@"
        valid_register_data["konfirmasi_password"] = "Abc def1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()
