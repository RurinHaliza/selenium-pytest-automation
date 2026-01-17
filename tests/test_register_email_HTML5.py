import pytest
from pages.register_page import RegisterPage

HTML5_INVALID_EMAILS = [
    "",
    "mahasiswa",
    "mahasiswa@",
    "mahasiswa@studentpolije",
    "mahasiswa@studentpolije.",
    "mahasiswa@.id",
    "mahasiswa @student.polije.ac.id",
]

@pytest.mark.parametrize("email", HTML5_INVALID_EMAILS)
def test_register_email_html5_validation(driver, email):
    register = RegisterPage(driver)
    register.open()

    register.fill_required_fields_except_email()
    register.input_email(email)
    register.submit()

    # HTML5 validation harus aktif
    assert register.is_html5_email_invalid()
