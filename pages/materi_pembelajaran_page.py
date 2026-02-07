from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MateriPembelajaranPage:

    # ===== SIDEBAR =====
    MENU_MATERI_PEMBELAJARAN = (
        By.XPATH,
        "//div[normalize-space()='Materi Pembelajaran']/ancestor::a"
    )

    SUBMENU_ENKAPSULASI = (
        By.XPATH,
        "//a[@href='/materi']//div[normalize-space()='Enkapsulasi']"
    )

    # ===== LEARNING STYLE UTAMA =====
    LEARNING_STYLE_TITLE = (
        By.XPATH,
        "//h5[normalize-space()='Learning Style Kamu 🎉']"
    )

    LEARNING_STYLE_VALUE = (
        By.XPATH,
        "//h5[normalize-space()='Learning Style Kamu 🎉']/following-sibling::p"
    )

    BUTTON_MULAI_BELAJAR_UTAMA = (
        By.XPATH,
        "//h5[normalize-space()='Learning Style Kamu 🎉']/following::a[normalize-space()='Mulai Belajar']"
    )

    # ===== PESAN ALTERNATIF =====
    PESAN_ALTERNATIF = (
        By.XPATH,
        "//h5[contains(text(),'Materi Sesuai Learning Style Kamu Sulit Dipahami')]"
    )

    # ===== CARD ALTERNATIF =====
    CARD_VISUAL = (
        By.XPATH,
        "//h5[normalize-space()='Visual']/following::a[normalize-space()='Mulai Belajar'][1]"
    )

    CARD_AUDITORY = (
        By.XPATH,
        "//h5[normalize-space()='Auditory']/following::a[normalize-space()='Mulai Belajar'][1]"
    )

    CARD_READ_WRITE = (
        By.XPATH,
        "//h5[normalize-space()='Read/ Write']/following::a[normalize-space()='Mulai Belajar'][1]"
    )

    # ===== JUDUL HALAMAN MATERI =====
    JUDUL_HALAMAN_MATERI = (
        By.XPATH,
        "//h4[@class='fw-bold mb-4']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== ACTIONS =====
    def open_from_sidebar(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MENU_MATERI_PEMBELAJARAN)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.SUBMENU_ENKAPSULASI)
        ).click()

    def click_mulai_belajar_utama(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_MULAI_BELAJAR_UTAMA)
        ).click()

    def click_visual(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CARD_VISUAL)
        ).click()

    def click_auditory(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CARD_AUDITORY)
        ).click()

    def click_read_write(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CARD_READ_WRITE)
        ).click()

    def get_learning_style_user(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LEARNING_STYLE_VALUE)
        ).text

    def get_judul_materi(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.JUDUL_HALAMAN_MATERI)
        ).text
