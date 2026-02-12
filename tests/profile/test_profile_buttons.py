import pytest


def test_email_tampil_sesuai_akun(profile_page):
    """
    Verifikasi email tampil sesuai akun dan tidak kosong
    """
    profile_page.wait_until_page_loaded()

    email = profile_page.get_email()

    assert email is not None
    assert email != ""
    assert "@" in email
    assert email.endswith(".ac.id") or email.endswith(".com")


def test_email_tidak_bisa_diedit(profile_page):
    """
    Verifikasi email memiliki attribute readonly
    """
    assert profile_page.is_email_readonly() is True


def test_nim_tampil_sesuai_akun(profile_page):
    """
    Verifikasi NIM tampil dan tidak kosong
    """
    nim = profile_page.get_nim()

    assert nim is not None
    assert nim != ""
    assert len(nim) >= 9
    assert len(nim) <= 10


def test_semester_tampil_sesuai_akun(profile_page):
    """
    Verifikasi semester memiliki selected value
    """
    semester = profile_page.get_selected_semester()

    assert semester is not None
    assert semester.isdigit()
    assert int(semester) >= 1
    assert int(semester) <= 8


def test_angkatan_tampil_sesuai_akun(profile_page):
    """
    Verifikasi angkatan memiliki selected value
    """
    angkatan = profile_page.get_selected_angkatan()

    assert angkatan is not None
    assert angkatan.isdigit()
    assert len(angkatan) == 4
