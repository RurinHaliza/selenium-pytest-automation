import pytest


@pytest.mark.usefixtures("driver")
class TestRegisterEmail:
    """
    RULE EMAIL:
    - Wajib diisi (HTML5)
    - Harus format email valid (HTML5)
    - Tidak boleh mengandung spasi
    - Domain wajib:
        @polije.ac.id
        @student.polije.ac.id
    - Validasi domain & email aktif menggunakan backend / JS
    """

    # =========================
    # NEGATIVE TEST CASES
    # =========================

    def test_email_kosong(self, register_page, valid_register_data):
        valid_register_data["email"] = ""
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_field_required("email")

    def test_email_hanya_spasi(self, register_page, valid_register_data):
        valid_register_data["email"] = "   "
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_field_required("email")

    def test_email_tanpa_at(self, register_page, valid_register_data):
        valid_register_data["email"] = "userpolije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("email")

    def test_email_angka_semua(self, register_page, valid_register_data):
        valid_register_data["email"] = "123456789"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("email")

    def test_nama_email_angka_semua(self, register_page, valid_register_data):
        valid_register_data["email"] = "12345678@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_email_simbol_semua(self, register_page, valid_register_data):
        valid_register_data["email"] = "@@@@@"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("email")

    def test_email_mengandung_spasi(self, register_page, valid_register_data):
        valid_register_data["email"] = "user @polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_html5_validation("email")

    def test_email_domain_bukan_polije(self, register_page, valid_register_data):
        valid_register_data["email"] = "user@gmail.com"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_email_domain_typo(self, register_page, valid_register_data):
        valid_register_data["email"] = "user@student.polije.co.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_email_tidak_aktif(self, register_page, valid_register_data):
        valid_register_data["email"] = "email.tidak.aktif@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_email_mengandung_dash(self, register_page, valid_register_data):
        valid_register_data["email"] = "user-test@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_email_mengandung_plus(self, register_page, valid_register_data):
        valid_register_data["email"] = "user+test@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("Email")

    def test_register_dua_kali_email_sama(self, register_page, valid_register_data):
        email = valid_register_data["email"]

        # Register pertama
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

        # Register kedua → email sama, nama & NIM beda
        register_page.open()

        data_kedua = valid_register_data.copy()
        data_kedua["email"] = email
        data_kedua["nama_lengkap"] = "User Kedua Unik"
        data_kedua["nim"] = "E41229999"

        register_page.fill_form(data_kedua)
        register_page.submit()

        assert register_page.has_error("Email")


    # =========================
    # POSITIVE TEST CASES
    # =========================
    
    def test_email_mengandung_underscore(self, register_page, valid_register_data):
        valid_register_data["email"] = "user_test@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_email_valid_polije(self, register_page, valid_register_data):
        valid_register_data["email"] = "dosen@polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_email_valid_student_polije(self, register_page, valid_register_data):
        valid_register_data["email"] = "mahasiswa@student.polije.ac.id"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()





