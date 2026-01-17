import pytest


@pytest.mark.usefixtures("driver")
class TestRegisterPassword:
    """
    RULE PASSWORD:
    - Wajib diisi (HTML5)
    - Minimal 8 karakter
    - Maksimal 12 karakter
    - Boleh mengandung spasi
    - Wajib mengandung:
      - Huruf besar
      - Huruf kecil
      - Angka atau karakter khusus
    - Validasi muncul setelah klik submit
    """

    # =========================
    # HTML5 VALIDATION
    # =========================

    def test_password_kosong(self, register_page, valid_register_data):
        """
        Password kosong → HTML5 required
        """
        valid_register_data["password"] = ""
        valid_register_data["konfirmasi_password"] = ""

        register_page.fill_form(valid_register_data)

        # TIDAK perlu submit, HTML5 sudah aktif
        assert register_page.is_field_required("password")

    # =========================
    # NEGATIVE TEST CASES (CUSTOM VALIDATION)
    # =========================

    def test_password_kurang_dari_minimum(self, register_page, valid_register_data):
        valid_register_data["password"] = "Ab1@"
        valid_register_data["konfirmasi_password"] = "Ab1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_lebih_dari_maksimum(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef1@xxxx"
        valid_register_data["konfirmasi_password"] = "Abcdef1@xxxx"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_tanpa_huruf_kapital(self, register_page, valid_register_data):
        valid_register_data["password"] = "abcdef1@"
        valid_register_data["konfirmasi_password"] = "abcdef1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_tanpa_huruf_kecil(self, register_page, valid_register_data):
        valid_register_data["password"] = "ABCDEF1@"
        valid_register_data["konfirmasi_password"] = "ABCDEF1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_tanpa_angka(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef@@"
        valid_register_data["konfirmasi_password"] = "Abcdef@@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_tanpa_karakter_khusus(self, register_page, valid_register_data):
        valid_register_data["password"] = "Abcdef12"
        valid_register_data["konfirmasi_password"] = "Abcdef12"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    @pytest.mark.parametrize(
        "password",
        [
            "12345678",    # angka semua
            "abcdefgh",    # huruf kecil semua
            "ABCDEFGH",    # huruf besar semua
            "@@@@@@@@",    # simbol semua
        ]
    )
    def test_password_komposisi_tidak_valid(
        self, register_page, valid_register_data, password
    ):
        valid_register_data["password"] = password
        valid_register_data["konfirmasi_password"] = password

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.has_error("Password")

    def test_password_mengandung_spasi(self, register_page, valid_register_data):
        """
        Spasi BOLEH, selama rule lain terpenuhi
        """
        valid_register_data["password"] = "Abc def1@"
        valid_register_data["konfirmasi_password"] = "Abc def1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()

    def test_password_tepat_minimum(self, register_page, valid_register_data):
        """
        Boundary value: tepat 8 karakter
        """
        valid_register_data["password"] = "Abcd1@xy"
        valid_register_data["konfirmasi_password"] = "Abcd1@xy"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()

    def test_password_tepat_maksimum(self, register_page, valid_register_data):
        """
        Boundary value: tepat 12 karakter
        """
        valid_register_data["password"] = "Abcd12@xyzQ"
        valid_register_data["konfirmasi_password"] = "Abcd12@xyzQ"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()

    # =========================
    # POSITIVE TEST CASE
    # =========================

    def test_password_valid(self, register_page, valid_register_data):
        """
        Password valid (huruf besar, kecil, angka, simbol)
        """
        valid_register_data["password"] = "Abcdef1@"
        valid_register_data["konfirmasi_password"] = "Abcdef1@"

        register_page.fill_form(valid_register_data)
        register_page.submit()

        assert register_page.is_register_success()
