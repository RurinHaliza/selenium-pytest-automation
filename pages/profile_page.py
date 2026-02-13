from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:

    # ===============================
    # LOCATORS
    # ===============================

    # --- Profile Display ---
    EMAIL_FIELD = (By.ID, "email")
    NAMA_LENGKAP_FIELD = (By.ID, "nama_lengkap")
    NIM_FIELD = (By.ID, "nim")
    SEMESTER_DROPDOWN = (By.ID, "semester")
    ANGKATAN_DROPDOWN = (By.ID, "angkatan")

    # --- Upload Foto ---
    FILE_INPUT = (By.ID, "profile_image")
    PROFILE_IMAGE = (By.ID, "uploadedAvatar")
    RESET_BUTTON = (By.XPATH, "//a[.//span[text()='Reset']]")

    # --- Buttons ---
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Simpan Perubahan')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Batal')]")

    # --- Error Messages ---
    ERROR_NAMA = (By.ID, "nama_lengkap-error")
    ERROR_NIM = (By.ID, "nim-error")
    ERROR_SEMESTER = (By.ID, "semester-error")
    ERROR_ANGKATAN = (By.ID, "angkatan-error")

    # --- Success Message ---
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")


    # ===============================
    # PROFILE DISPLAY METHODS
    # ===============================

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_email(self):
        return self.driver.find_element(*self.EMAIL_FIELD).get_attribute("value")

    def is_email_readonly(self):
        return self.driver.find_element(*self.EMAIL_FIELD).get_attribute("readonly") is not None

    def get_nama_lengkap(self):
        return self.driver.find_element(*self.NAMA_LENGKAP_FIELD).get_attribute("value")

    def get_nim(self):
        return self.driver.find_element(*self.NIM_FIELD).get_attribute("value")

    def get_selected_semester(self):
        select = Select(self.driver.find_element(*self.SEMESTER_DROPDOWN))
        return select.first_selected_option.text

    def get_selected_angkatan(self):
        select = Select(self.driver.find_element(*self.ANGKATAN_DROPDOWN))
        return select.first_selected_option.text

    # ===============================
    # EDIT METHODS
    # ===============================

    def set_nama_lengkap(self, name):
        field = self.driver.find_element(*self.NAMA_LENGKAP_FIELD)
        field.clear()
        field.send_keys(name)

    def set_nim(self, nim):
        field = self.driver.find_element(*self.NIM_FIELD)
        field.clear()
        field.send_keys(nim)

    def select_semester(self, value):
        Select(self.driver.find_element(*self.SEMESTER_DROPDOWN)).select_by_value(value)

    def select_angkatan(self, value):
        Select(self.driver.find_element(*self.ANGKATAN_DROPDOWN)).select_by_value(value)

    # ===============================
    # UPLOAD METHODS
    # ===============================

    def upload_photo(self, file_path):
        self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)

    def get_profile_image_src(self):
        return self.driver.find_element(*self.PROFILE_IMAGE).get_attribute("src")

    def click_reset_photo(self):
        wait = WebDriverWait(self.driver, 10)

        reset_btn = wait.until(
            EC.element_to_be_clickable(self.RESET_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", reset_btn)
        self.driver.execute_script("arguments[0].click();", reset_btn)


    # ===============================
    # BUTTON ACTIONS
    # ===============================

    def click_save(self):
        wait = WebDriverWait(self.driver, 10)

        save_btn = wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )

        # scroll dulu supaya tidak ketutup elemen
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)

        wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_btn.click()

    def click_cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    # ===============================
    # UTILITIES
    # ===============================

    def refresh_page(self):
        self.driver.refresh()

    def wait_until_page_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(self.EMAIL_FIELD)
        )

    # ===============================
    # VALIDATION MESSAGE METHODS
    # ===============================

    def get_error_nama(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_NAMA)
        ).text

    def get_error_nim(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_NIM)
        ).text

    def get_error_semester(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_SEMESTER)
        ).text

    def get_error_angkatan(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_ANGKATAN)
        ).text

    def wait_until_reload_after_save(self):
        self.wait.until(
            EC.presence_of_element_located(self.EMAIL_FIELD)
        )
