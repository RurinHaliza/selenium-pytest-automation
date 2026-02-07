from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MateriPage:

    # ===== SIDEBAR =====
    SIDEBAR = (By.ID, "learningStyleSidebar")

    BTN_VISUAL = (
        By.XPATH,
        "//div[@id='learningStyleSidebar']//h6[normalize-space()='Visual']/following-sibling::a"
    )

    BTN_AUDITORY = (
        By.XPATH,
        "//div[@id='learningStyleSidebar']//h6[normalize-space()='Auditory']/following-sibling::a"
    )

    # ===== JUDUL HALAMAN =====
    TITLE_VISUAL = (By.XPATH, "//h4[normalize-space()='Materi Visual']")
    TITLE_AUDITORY = (By.XPATH, "//h4[normalize-space()='Materi Auditory']")

    # ===== MEDIA =====
    VISUAL_IMAGE = (By.XPATH, "//img[@alt='Gambar Materi']")
    AUDIO_PLAYER = (By.XPATH, "//audio")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== SIDEBAR =====
    def sidebar_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SIDEBAR))

    def go_to_visual(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_VISUAL)).click()

    def go_to_auditory(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_AUDITORY)).click()

    # ===== ASSERTION =====
    def visual_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE_VISUAL))
        self.wait.until(EC.visibility_of_element_located(self.VISUAL_IMAGE))

    def auditory_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE_AUDITORY))
        self.wait.until(EC.visibility_of_element_located(self.AUDIO_PLAYER))
