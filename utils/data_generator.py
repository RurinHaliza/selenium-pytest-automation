import random
import string
import time


def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_number(length=10):
    return ''.join(random.choices(string.digits, k=length))


def valid_nama_lengkap():
    return f"User {random_string(5)}"


def valid_nim():
    return random_number(9)


def valid_semester():
    return str(random.randint(1, 8))


def valid_angkatan():
    return str(random.randint(2022, 2025))


def valid_email():
    timestamp = int(time.time() * 1000)
    return f"user{timestamp}@student.polije.ac.id"


def valid_password():
    return "Test@1234"


def generate_valid_register_data():
    """
    Data VALID & lengkap untuk form register
    """
    return {
        "nama": valid_nama_lengkap(),
        "nim": valid_nim(),
        "semester": valid_semester(),
        "angkatan": valid_angkatan(),
        "email": valid_email(),
        "password": valid_password(),
    }

def generate_valid_nim():
    """
    NIM valid:
    - huruf + angka
    - panjang 9–10
    Contoh: E41222789
    """
    prefix = random.choice(string.ascii_uppercase)
    digits = ''.join(random.choices(string.digits, k=random.randint(8, 9)))
    return prefix + digits
