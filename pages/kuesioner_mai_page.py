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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(self.TITLE)
        )

    def answer_question(self, question_number, option_index=0):
        """
        option_index: 0–3 (nilai 0–3)
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

    def answer_all_questions(self, total_questions=52):
        for i in range(1, total_questions + 1):
            self.answer_question(i)

    def submit(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        btn.click()
