import pytest
from pages.register_page import RegisterPage

CUSTOM_INVALID_EMAILS = [
    "mahasiswa@gmail.com",
    "mahasiswa@studentpolije.ac.id",  # prefix salah
    "12345678@student.polije.ac.id"
]

CUSTOM_VALID_EMAILS = [
    "mahasiswa@student.polije.ac.id"
]

@pytest.mark.parametrize("email", CUSTOM_INVALID_EMAILS)
def test_register_email_custom_invalid(driver, email):
    register = RegisterPage(driver)
    register.open()

    register.fill_required_fields_except_email()
    register.input_email(email)
    register.submit()

    assert register.is_custom_email_error_displayed()


@pytest.mark.parametrize("email", CUSTOM_VALID_EMAILS)
def test_register_email_custom_valid(driver, email):
    register = RegisterPage(driver)
    register.open()

    register.fill_required_fields_except_email()
    register.input_email(email)
    register.submit()

    assert not register.is_custom_email_error_displayed()
