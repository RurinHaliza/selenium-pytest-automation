from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    URL = "https://hypermedialearning.sanggadewa.my.id/dashboard"

    # ===== POPUP (MODAL) =====
    POPUP_MODAL = (By.ID, "kuesionerModal")
    BTN_ISI_KUESIONER_POPUP = (
        By.XPATH, "//div[@id='kuesionerModal']//a[contains(text(),'Isi Kuesioner')]"
    )
    BTN_TUTUP_POPUP = (
        By.XPATH, "//div[@id='kuesionerModal']//button[contains(text(),'Tutup')]"
    )
    BTN_CLOSE_X = (
        By.XPATH, "//div[@id='kuesionerModal']//button[@aria-label='Close']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    # ======================
    # POPUP METHODS
    # ======================

    def is_popup_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.POPUP_MODAL)
            )
            return True
        except:
            return False

    def click_isi_kuesioner(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BTN_ISI_KUESIONER_POPUP)
        ).click()

    def close_popup_with_tutup(self):
        btn = self.wait.until(
            EC.visibility_of_element_located(self.BTN_TUTUP_POPUP)
        )
        btn.click()

        self.wait.until(
            EC.invisibility_of_element_located(self.POPUP_MODAL)
        )


    def close_popup_with_x(self):
        btn = self.wait.until(
            EC.visibility_of_element_located(self.BTN_CLOSE_X)
        )
        btn.click()
        self.wait_popup_disappear()


    def is_redirected_to_kuesioner(self):
        self.wait.until(lambda d: "kuesioner" in d.current_url)
        return True
    
    def wait_popup_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.POPUP_MODAL)
        )


