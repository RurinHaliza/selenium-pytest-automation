from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KuesionerMAIPage:

    TITLE = (
        By.XPATH,
        "//h3[contains(text(),'Kuesioner Metakognitif')]"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Simpan Jawaban']"
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
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(self.TITLE)
        )

    def answer_question_mai(self, question_number, option_index=0):
        """
        option_index: 0–4 (nilai 0–4)
        """
        radios = self.driver.find_elements(
            By.NAME, f"soal{question_number}"
        )

        target = radios[option_index]

        # WAJIB scroll agar tidak intercepted
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            target
        )

        self.wait.until(EC.element_to_be_clickable(target)).click()

    def answer_question_ls(self, question_number, option_index=0):
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

    def answer_all_questions_ls(self, total_questions=16):
        for i in range(1, total_questions + 1):
            self.answer_question_ls(i)

    def answer_all_questions_mai(self, total_questions=52):
        for i in range(1, total_questions + 1):
            self.answer_question_mai(i)

    def submit(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        btn.click()

    def open_from_sidebar(self):
            self.wait.until(
                EC.element_to_be_clickable(self.KUESIONER_MENU)
            ).click()

    def click_mulai_kuesioner(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MULAI_KUESIONER_BUTTON)
        ).click()  
