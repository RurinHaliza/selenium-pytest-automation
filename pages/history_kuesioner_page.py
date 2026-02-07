from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HistoryKuesionerPage:

    URL = "https://hypermedialearning.sanggadewa.my.id/history_quis"

    # ===== SIDEBAR =====
    SIDEBAR_HISTORY = (
        By.XPATH,
        "//li[contains(@class,'menu-item') and .//div[normalize-space()='History Kuisioner']]"
    )

    # ===== SKOR GAYA BELAJAR =====
    SCORE_CONTAINER = (By.CSS_SELECTOR, "div.card")
    SCORE_LABELS = (By.CSS_SELECTOR, "div.score-label")
    SCORE_VALUES = (By.CSS_SELECTOR, "div.score-value")
    
    LEARNING_STYLE_CARD = (
    By.XPATH,
    "//div[contains(@class,'card') and .//div[text()='Visual']]"
    )

    LEARNING_STYLE_LABELS = (
        By.XPATH,
        "//div[contains(@class,'card') and .//div[text()='Visual']]//div[@class='score-label']"
    )

    LEARNING_STYLE_VALUES = (
        By.XPATH,
        "//div[contains(@class,'card') and .//div[text()='Visual']]//div[@class='score-value']"
    )

    LEARNING_STYLE_ITEMS = (
    By.CSS_SELECTOR,
    "div.card.shadow.border-0.p-4 > div.row.text-center > div.col-6.col-md-3"
    )

    # ===== PROGRESS =====
    PROGRESS_BAR = (By.CSS_SELECTOR, "div.progress-bar")
    PROGRESS_TEXT = (
        By.XPATH,
        "//small[contains(text(),'pertanyaan dijawab')]"
    )

    # ===== GAYA BELAJAR DOMINAN =====
    DOMINANT_STYLE_TEXT = (
        By.XPATH,
        "//h2[contains(@class,'fw-bold')]"
    )

    BTN_MULAI_BELAJAR = (
        By.XPATH,
        "//a[contains(@href,'/materi') and contains(.,'Mulai')]"
    )

    # ===== KM & RM =====
    KM_VALUE = (
        By.XPATH,
        "//div[normalize-space()='KM']/following-sibling::div[contains(@class,'score-value')]"
    )

    RM_VALUE = (
        By.XPATH,
        "//div[normalize-space()='RM']/following-sibling::div[contains(@class,'score-value')]"
    )

    # ===== RIWAYAT =====
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")

    # ===== AKSI =====
    BTN_MULAI_BELAJAR = (
    By.XPATH,
    "//a[contains(@href,'/materi')]"
    )

    BTN_UBAH = (
        By.XPATH,
        "//a[contains(@href,'kuesioner')]"
    )

    BTN_UNDUH = (
        By.XPATH,
        "//a[contains(@href,'user-result')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def is_page_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.SIDEBAR_HISTORY))
        return True

    def get_scores(self):
        """
        Return skor gaya belajar saja.
        PASSED = benar-benar 4 gaya belajar.
        """
        items = self.wait.until(
            lambda d: d.find_elements(*self.LEARNING_STYLE_ITEMS)
        )

        assert len(items) == 4, f"Expected 4 learning styles, found {len(items)}"

        scores = {}
        for item in items:
            label = item.find_element(By.CSS_SELECTOR, ".score-label").text.strip()
            value = item.find_element(By.CSS_SELECTOR, ".score-value").text.strip()
            scores[label] = value

        return scores

    def get_score_labels(self):
        # tunggu card halaman muncul dulu
        self.wait.until(
            EC.presence_of_element_located(self.SCORE_CONTAINER)
        )

        # baru ambil labels
        self.wait.until(
            lambda d: len(d.find_elements(*self.SCORE_LABELS)) >= 4
        )

        return [
            e.text.strip()
            for e in self.driver.find_elements(*self.SCORE_LABELS)
            if e.text.strip() != ""
        ]
    
    def get_score_values(self):
        self.wait.until(
            lambda d: all(
                e.text.strip().isdigit()
                for e in d.find_elements(*self.LEARNING_STYLE_VALUES)
            )
        )
        return [e.text.strip() for e in self.driver.find_elements(*self.LEARNING_STYLE_VALUES)]

    def get_progress_value(self):
        bar = self.wait.until(EC.presence_of_element_located(self.PROGRESS_BAR))
        return bar.get_attribute("aria-valuenow")

    def get_progress_text(self):
        return self.driver.find_element(*self.PROGRESS_TEXT).text

    def get_dominant_style(self):
        return self.wait.until(
            EC.presence_of_element_located(self.DOMINANT_STYLE_TEXT)
        ).text.strip()

    def click_mulai(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.BTN_MULAI_BELAJAR)
        )

        # Scroll ke elemen (cukup)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )

        # Klik pakai JS (paling stabil untuk <a>)
        self.driver.execute_script("arguments[0].click();", button)

    def get_km_value(self):
        return self.driver.find_element(*self.KM_VALUE).text.lower()

    def get_rm_value(self):
        return self.driver.find_element(*self.RM_VALUE).text.lower()

    def get_history_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)

    def click_ubah(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_UBAH)).click()

    def click_unduh(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BTN_UNDUH))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)

