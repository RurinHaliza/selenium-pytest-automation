from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    URL = "https://hypermedialearning.sanggadewa.my.id/register"

    # ===============================
    # LOCATORS
    # ===============================
    NAMA_LENGKAP = (By.ID, "nama_lengkap")
    NIM = (By.ID, "nim")
    SEMESTER = (By.ID, "semester")
    ANGKATAN = (By.ID, "angkatan")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.NAME, "password")
    KONFIRMASI_PASSWORD = (By.NAME, "password_confirmation")
    BUTTON_DAFTAR = (By.XPATH, "//button[@type='submit']")

    ERROR_MESSAGE = (By.CLASS_NAME, "invalid-feedback")
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Email harus menggunakan domain')]"
    )

    # ===============================
    # INIT
    # ===============================
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===============================
    # PAGE ACTIONS
    # ===============================
    def open(self):
        self.driver.get(self.URL)

    def fill_nama_lengkap(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.NAMA_LENGKAP)
        )
        field.clear()
        field.send_keys(value)

    def fill_nim(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.NIM)
        )
        field.clear()
        field.send_keys(value)

    def fill_semester(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.SEMESTER)
        )
        field.clear()
        field.send_keys(value)

    def fill_angkatan(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.ANGKATAN)
        )
        field.clear()
        field.send_keys(value)

    def fill_email(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        field.clear()
        field.send_keys(value)

    def fill_password(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        field.clear()
        field.send_keys(value)

    def fill_confirm_password(self, value: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.KONFIRMASI_PASSWORD)
        )
        field.clear()
        field.send_keys(value)

    def click_daftar(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_DAFTAR)
        ).click()

    # ===============================
    # HELPER / BUSINESS METHODS
    # ===============================
    def fill_form(self, data: dict):
        self.fill_nama_lengkap(data["nama_lengkap"])
        self.fill_nim(data["nim"])
        self.fill_semester(data["semester"])
        self.fill_angkatan(data["angkatan"])
        self.fill_email(data["email"])
        self.fill_password(data["password"])
        
        if "konfirmasi_password" in data:
            self.fill_confirm_password(data["konfirmasi_password"])

        pwd = self.driver.find_element(*self.PASSWORD).get_attribute("value")
        cpwd = self.driver.find_element(*self.KONFIRMASI_PASSWORD).get_attribute("value")

        print("PASSWORD FIELD :", repr(pwd))
        print("CONFIRM FIELD  :", repr(cpwd))



    def submit(self):
        """Alias agar test lebih readable"""
        self.click_daftar()

    def get_error_messages(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return [el.text for el in elements if el.text.strip()]

    def has_error(self, field_name: str) -> bool:
        """
        Mengecek apakah error message terkait field tertentu muncul
        """
        return any(
            field_name.lower() in err.lower()
            for err in self.get_error_messages()
        )

    def is_email_domain_error_displayed(self) -> bool:
        try:
            return self.driver.find_element(
                *self.EMAIL_ERROR_MESSAGE
            ).is_displayed()
        except Exception:
            return False

    def is_register_success(self) -> bool:
        """
        Register dianggap sukses jika terjadi redirect dari halaman register.
        """
        self.wait.until(
            lambda d: d.current_url != self.URL
        )
        return True

    def is_field_required(self, label_text: str) -> bool:
        """
        Mengecek apakah field dengan label tertentu memiliki atribut required
        (HTML5 native validation)
        """
        fields = {
            "nama_lengkap": self.NAMA_LENGKAP,
            "NIM": self.NIM,
            "nim": self.NIM,
            "semester": self.SEMESTER,
            "angkatan": self.ANGKATAN,
            "email": self.EMAIL,
            "password": self.PASSWORD,
            "konfirmasi_password":self.KONFIRMASI_PASSWORD,
        }

        locator = fields.get(label_text)
        if not locator:
            raise ValueError(f"Field '{label_text}' tidak dikenali")

        element = self.driver.find_element(*locator)
        return element.get_attribute("required") is not None

    def get_value(self, field_name: str) -> str:
        field = self.get_field(field_name)
        return field.get_attribute("value")

    def get_field(self, field_name: str):
        fields = {
            "nama_lengkap": self.NAMA_LENGKAP,
            "NIM": self.NIM,
            "nim": self.NIM,
            "semester": self.SEMESTER,
            "Semester": self.SEMESTER,
            "angkatan": self.ANGKATAN,
            "Angkatan": self.ANGKATAN,
            "email": self.EMAIL,
            "password": self.PASSWORD,
            "konfirmasi_password":self.KONFIRMASI_PASSWORD,
        }

        locator = fields.get(field_name)
        if not locator:
            raise ValueError(f"Field '{field_name}' tidak dikenali")

        return self.driver.find_element(*locator)
    
    def has_html5_validation(self, field_name: str) -> bool:
        field = self.get_field(field_name)
        return field.get_attribute("validationMessage") != ""



