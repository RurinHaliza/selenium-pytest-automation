from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ResumePembelajaranPage:

    # ===== Locator =====
    PAGE_TITLE = (By.XPATH, "//h4[normalize-space()='Resume Pembelajaran']")

    EMPTY_MESSAGE = (
    By.CSS_SELECTOR,
    "div.text-center.text-muted"
)

    RESUME_CARD = (By.CSS_SELECTOR, "div.card")
    RESUME_CONTENT = (By.CSS_SELECTOR, "div.card-body pre")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== Assertions / Getters =====
    def page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))

    
    def is_empty_message_displayed(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(self.EMPTY_MESSAGE)
            )
            return True
        except TimeoutException:
            return False

    def is_resume_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RESUME_CARD)
        )

    def get_resume_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RESUME_CONTENT)
        ).text
