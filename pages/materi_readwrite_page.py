from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MateriReadWritePage:

    # ===== Locator =====
    PAGE_TITLE = (By.XPATH, "//h4[normalize-space()='Materi Read / Write']")
    TEXT_MATERI = (By.XPATH, "//strong[text()='Teks:']/following-sibling::pre")
    
    RANGKUMAN_TEXTAREA = (By.ID, "rangkuman")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Kirim Rangkuman']")
    
    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class,'alert-success')]")
    TUGAS_RANGKUMAN_LABEL = (By.XPATH,"//label[@for='rangkuman']//strong[normalize-space()='Tugas Rangkuman:']")

    
    # Sidebar navigasi materi lain
    SIDEBAR_VISUAL = (
        By.XPATH,
        "//div[@id='learningStyleSidebar']//h6[normalize-space()='Visual']/following-sibling::a"
    )
    SIDEBAR_AUDITORY = (
        By.XPATH,
        "//div[@id='learningStyleSidebar']//h6[normalize-space()='Auditory']/following-sibling::a"
    )
    SIDEBAR_KINESTHETIC = (
        By.XPATH,
        "//div[@id='learningStyleSidebar']//h6[normalize-space()='Kinesthetic']/following-sibling::a"
    )
    ERROR_ALERT = (By.XPATH, "//div[contains(@class,'alert-danger')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== Actions =====
    def page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))

    def get_text_materi(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TEXT_MATERI)
        ).text

    def input_rangkuman(self, text):
        textarea = self.wait.until(
            EC.visibility_of_element_located(self.RANGKUMAN_TEXTAREA)
        )
        textarea.clear()
        textarea.send_keys(text)

    def submit_rangkuman(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

    def success_message_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT)
        )

    # ===== Sidebar navigation =====
    def go_to_visual(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDEBAR_VISUAL)).click()

    def go_to_auditory(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDEBAR_AUDITORY)).click()

    def go_to_kinesthetic(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDEBAR_KINESTHETIC)).click()

    def error_message_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_ALERT)
        )
