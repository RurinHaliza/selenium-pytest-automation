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

    MODAL_KUESIONER = (By.ID, "kuesionerModal")

    BTN_TUTUP_MODAL = (
        By.XPATH,
        "//button[contains(text(),'Nanti') or contains(text(),'Tutup')]"
    )

    KM_VALUE = (
        By.XPATH,
        "//span[normalize-space()='Knowledge of Metakognitif (KM)']"
        "/ancestor::div[contains(@class,'card')]"
        "//span[normalize-space()='Nilai']/following-sibling::span"
)

    RM_VALUE = (
        By.XPATH,
        "//span[normalize-space()='Regulation of Metakognitif (RM)']"
        "/ancestor::div[contains(@class,'card')]"
        "//span[normalize-space()='Nilai']/following-sibling::span"
)
    
    LEARNING_STYLE_VALUE = (
        By.XPATH,
        "//span[normalize-space()='Learning Style']"
        "/ancestor::div[contains(@class,'card')]"
        "//span[normalize-space()='Gaya Belajar']/following-sibling::span"
)
    
    PENGISIAN_KUESIONER_SECTION = (
        By.XPATH,
        "//h6[normalize-space()='Pengisian Kuesioner']/ancestor::div[contains(@class,'card')]"
)
  
    KUESIONER_VARK_MAI_TEXT = (
        By.XPATH,
        "//td[normalize-space()='Kuesioner VARK dan MAI']"
)
    
    ISI_KUESIONER_BUTTON = (
    By.XPATH,
    "//a[@href='https://hypermedialearning.sanggadewa.my.id/kuesioner-panduan']"
)



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

# POM for test dashboard PopUp

    def is_popup_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.POPUP_MODAL)
            )
            return True
        except:
            return False

    def click_isi_kuesioner_pop_up(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BTN_ISI_KUESIONER_POPUP)
        ).click()

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

#POM for Test Dashboard KMRM 
   
    def close_kuesioner_popup_if_present(self):
        btn = self.wait.until(
            EC.visibility_of_element_located(self.BTN_CLOSE_X)
        )
        btn.click()
        self.wait_popup_disappear()
    
    def get_km_status_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.KM_VALUE)
        ).text.strip()

    def get_rm_status_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RM_VALUE)
        ).text.strip()

    def is_km_not_filled(self):
        return self.get_km_status_text() == "()"

    def is_rm_not_filled(self):
        return self.get_rm_status_text() == "()"

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

#POM for Learning Style

    def get_learning_style_text(self) -> str:
        el = self.wait.until(
            EC.visibility_of_element_located(self.LEARNING_STYLE_VALUE)
        )
        return el.text.strip()
    
    def is_learning_style_not_filled(self) -> bool:
        return self.get_learning_style_text() == "(Tidak diketahui)"

    def is_learning_style_filled(self) -> bool:
        text = self.get_learning_style_text()
        return text != "" and text != "(Tidak diketahui)"

#POM for Pengisian Kuesioner
    def is_pengisian_kuesioner_section_visible(self) -> bool:
            try:
                self.wait.until(
                    EC.visibility_of_element_located(
                        self.PENGISIAN_KUESIONER_SECTION
                    )
                )
                return True
            except:
                return False

    def is_kuesioner_vark_mai_visible(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.KUESIONER_VARK_MAI_TEXT
                )
            )
            return True
        except:
            return False

    def click_isi_kuesioner(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ISI_KUESIONER_BUTTON
            )
        ).click()

  




    




            
            




