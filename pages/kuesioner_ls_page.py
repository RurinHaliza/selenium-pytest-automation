from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KuesionerLSPage:
    
    DASHBOARD_MENU = (
        By.XPATH,
        "//a[contains(@href,'dashboard') or .//div[normalize-space()='Dashboard']]"
    )

    SUBMIT_BUTTON = (
        By.XPATH, "//button[normalize-space()='Simpan Jawaban']"
    )

    KUESIONER_MENU = (
        By.XPATH,
        "//a[contains(@href,'kuesioner-panduan') and .//div[normalize-space()='Kuesioner']]"
    )

    MULAI_KUESIONER_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'/kuesioner-ls') and normalize-space()='Mulai Kuesioner']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_from_sidebar(self):
        self.wait.until(
            EC.element_to_be_clickable(self.KUESIONER_MENU)
        ).click()

    def click_mulai_kuesioner(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MULAI_KUESIONER_BUTTON)
        ).click()

    def answer_question(self, question_number, option_index=0):
        """
        option_index: 0-3 (LS punya 4 opsi)
        """
        options = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.NAME, f"soal{question_number}")
            )
        )

        option = options[option_index]

        # WAJIB scroll dulu
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", option
        )

        self.wait.until(EC.element_to_be_clickable(option)).click()


    def answer_all_questions(self, total_questions=16):
        for i in range(1, total_questions + 1):
            self.answer_question(i)

    def submit(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )

        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def force_navigate_to_dashboard(self):
        menu = self.wait.until(
            EC.presence_of_element_located(self.DASHBOARD_MENU)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", menu
        )

        self.wait.until(EC.element_to_be_clickable(self.DASHBOARD_MENU)).click()

