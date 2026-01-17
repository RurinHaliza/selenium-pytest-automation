import pytest


@pytest.mark.usefixtures("driver")
class TestRegisterSemester:
    """
    RULE SEMESTER:
    - Wajib diisi (HTML5)
    - Hanya angka
    - Range 1 - 14
    """

    # =========================
    # NEGATIVE TEST CASES
    # =========================

    def test_semester_kosong(self, register_page, valid_register_data):
        valid_register_data["semester"] = ""
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_field_required("semester")

    def test_semester_hanya_spasi(self, register_page, valid_register_data):
        valid_register_data["semester"] = "   "
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_field_required("semester")

    def test_semester_huruf(self, register_page, valid_register_data):
        valid_register_data["semester"] = "abc"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("semester")

    def test_semester_simbol(self, register_page, valid_register_data):
        valid_register_data["semester"] = "@@"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("semester")

    def test_semester_kurang_dari_minimum(self, register_page, valid_register_data):
        valid_register_data["semester"] = "0"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("semester")

    def test_semester_lebih_dari_maksimum(self, register_page, valid_register_data):
        valid_register_data["semester"] = "15"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.has_error("semester")

    # =========================
    # POSITIVE TEST CASES
    # =========================

    def test_semester_valid_minimum(self, register_page, valid_register_data):
        valid_register_data["semester"] = "1"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_semester_valid_tengah(self, register_page, valid_register_data):
        valid_register_data["semester"] = "8"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()

    def test_semester_valid_maksimum(self, register_page, valid_register_data):
        valid_register_data["semester"] = "14"
        register_page.fill_form(valid_register_data)
        register_page.submit()
        assert register_page.is_register_success()
