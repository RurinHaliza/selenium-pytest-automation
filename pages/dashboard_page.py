from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


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

    

    STATUS_KM = (
        By.XPATH, "//*[contains(text(),'') and contains(text(),'Nilai')]"
    )

    STATUS_RM = (
        By.XPATH, "//*[contains(text(),'') and contains(text(),'Nilai')]"
    )

    MODAL_KUESIONER = (By.ID, "kuesionerModal")

    BTN_TUTUP_MODAL = (
        By.XPATH,
        "//button[contains(text(),'Nanti') or contains(text(),'Tutup')]"
    )

    KM_VALUE = (
    By.XPATH,
    "//span[normalize-space()='Nilai']/following-sibling::span"
    )

    RM_VALUE = (
    By.XPATH,
    "//span[normalize-space()='Nilai']/following-sibling::span"
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

    def get_km_status_text(self) -> str:
        el = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_KM)
        )
        return el.text


    def get_rm_status_text(self) -> str:
        el = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_RM)
        )
        return el.text
    
    def is_km_not_filled(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.STATUS_KM)
            )
            return True
        except:
            return False


    def is_rm_not_filled(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.STATUS_RM)
            )
            return True
        except:
            return False
        
    def close_kuesioner_popup_if_present(self):
        btn = self.wait.until(
            EC.visibility_of_element_located(self.BTN_CLOSE_X)
        )
        btn.click()
        self.wait_popup_disappear()

    def get_km_status_text(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_KM)
        )
        return el.text.strip()
    
    def get_rm_status_text(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_RM)
        )
        return el.text.strip()
    
    def get_km_status_text_sudah_isi(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.KM_VALUE)
        )
        return el.text.strip()
    
    def get_rm_status_text_sudah_isi(self):
        el = self.wait.until(
            EC.visibility_of_element_located(self.RM_VALUE)
        )
        return el.text.strip()

    def _extract_score(self, text: str):
        match = re.search(r"\((.*?)\)", text)
        if not match:
            return None
        value = match.group(1).strip()
        return value if value else None


    def is_km_not_filled(self):
        text = self.get_km_status_text()
        return self._extract_score(text) is None


    def is_rm_not_filled(self):
        text = self.get_rm_status_text()
        return self._extract_score(text) is None
    
    def is_km_filled(self):
        el = self.wait.until(
        EC.visibility_of_element_located(self.KM_VALUE)
    )
        return el.text.strip()
    
    def is_rm_filled(self):
        el = self.wait.until(
        EC.visibility_of_element_located(self.RM_VALUE)
    )
        return el.text.strip()




    




            
            




