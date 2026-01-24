from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://hypermedialearning.sanggadewa.my.id/login"
    DASHBOARD_URL_PART = "/dashboard"

    # ===============================
    # LOCATORS
    # ===============================
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    REMEMBER_ME = (By.NAME, "remember")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")

    ERROR_MESSAGE = (By.CLASS_NAME, "invalid-feedback")
    GLOBAL_ERROR = (
        By.XPATH,
        "//*[contains(text(),'These credentials do not match our records')]"
    )

    SSO_GOOGLE_BUTTON = (By.XPATH, "//a[contains(@href,'/auth/google')]")

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

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_LOGIN)
        ).click()

    def click_remember_me(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.REMEMBER_ME)
        )
        if not checkbox.is_selected():
            checkbox.click()

    def click_google_sso(self):
        self.wait.until(
            EC.element_to_be_clickable(self.GOOGLE_SSO_BUTTON)
        ).click()

    # ===============================
    # BUSINESS / HELPER METHODS
    # ===============================
    def login(self, email: str, password: str):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    def is_login_success(self) -> bool:
        try:
            self.wait.until(
                lambda d: self.DASHBOARD_URL_PART in d.current_url
            )
            return True
        except:
            return False

    def is_login_failed(self) -> bool:
        return self.has_error_message()

    def has_error_message(self) -> bool:
        return any(
            el.text.strip()
            for el in self.driver.find_elements(*self.ERROR_MESSAGE)
        )

    def has_global_error(self) -> bool:
        try:
            return self.driver.find_element(
                *self.GLOBAL_ERROR
            ).is_displayed()
        except:
            return False

    def is_field_required(self, field_name: str) -> bool:
        fields = {
            "email": self.EMAIL,
            "password": self.PASSWORD
        }

        locator = fields.get(field_name)
        if not locator:
            raise ValueError(f"Field '{field_name}' tidak dikenali")

        element = self.driver.find_element(*locator)
        return element.get_attribute("required") is not None

    def get_email_validation_message(self):
        email = self.driver.find_element(By.ID, "email")
        return self.driver.execute_script(
            "return arguments[0].validationMessage;",
            email
        )

    def submit(self):
        self.click_login()

    def has_html5_validation(self, field_name: str) -> bool:
        field = self.get_field(field_name)
        return field.get_attribute("validationMessage") != ""
    
    def get_field(self, field_name: str):
        fields = {
            "email": self.EMAIL,
            "password": self.PASSWORD,
        }

        locator = fields.get(field_name)
        if not locator:
            raise ValueError(f"Field '{field_name}' tidak dikenali di LoginPage")

        return self.driver.find_element(*locator)
    
    def click_remember_me(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.REMEMBER_ME)
        )
        if not checkbox.is_selected():
            checkbox.click()

    def is_remember_me_checked(self) -> bool:
        checkbox = self.driver.find_element(*self.REMEMBER_ME)
        return checkbox.is_selected()

    def click_sso_google(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SSO_GOOGLE_BUTTON)
        ).click()

    def is_redirected_to_google(self) -> bool:
        self.wait.until(
            lambda d: "accounts.google.com" in d.current_url
        )
        return "accounts.google.com" in self.driver.current_url





