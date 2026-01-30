from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KuesionerPanduanPage:

    URL = "https://hypermedialearning.sanggadewa.my.id/kuesioner-panduan"

    # ===== LOCATORS =====
    KUESIONER_MENU = (
        By.XPATH,
        "//a[contains(@href,'kuesioner-panduan') and .//div[normalize-space()='Kuesioner']]"
    )

    MULAI_KUESIONER_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'/kuesioner-ls') and normalize-space()='Mulai Kuesioner']"
    )

    BANTUAN_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'wa.me') and contains(normalize-space(),'Bantuan')]"
    )

    # ===== INIT =====
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ===== ACTIONS =====
    def open_from_sidebar(self):
        self.wait.until(
            EC.element_to_be_clickable(self.KUESIONER_MENU)
        ).click()

    def click_mulai_kuesioner(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MULAI_KUESIONER_BUTTON)
        ).click()

    def click_bantuan(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BANTUAN_BUTTON)
        ).click()

    # ===== ASSERTIONS =====
    def is_on_panduan_page(self) -> bool:
        return "kuesioner-panduan" in self.driver.current_url
    
    

