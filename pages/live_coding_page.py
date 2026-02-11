from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class LiveCodingPage:

    # ===== LOCATORS =====
    PAGE_TITLE = (By.XPATH, "//h4[contains(text(),'Live Coding')]")
    EXPECTED_OUTPUT = (By.XPATH, "//strong[contains(text(),'Hasil Output')]")
    CODE_EDITOR = (By.ID, "editor")
    SUBMIT_BUTTON = (By.ID, "submit-code")
    ERROR_404_TEXT = "404"

    #alert / result
    RESULT_MESSAGE = (By.ID, "result")
    MODAL = (By.CLASS_NAME, "modal-dialog")
    CLOSE_BUTTON = (By.XPATH, "//button[normalize-space()='Tutup']")
    PREVIOUS_BUTTON = (By.XPATH, "//a[contains(text(),'Sebelumnya')]")
    NEXT_BUTTON = (By.XPATH, "//a[contains(text(),'Selanjutnya')]")
    OTHER_MENU = (By.XPATH, "//a[contains(@href,'/materi/visual/')]")
    CONFIRM_MODAL = (By.CLASS_NAME, "modal")
    CONFIRM_TEXT = (By.CLASS_NAME, "modal-body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== PAGE ACTIONS =====
    def is_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return True

    def get_expected_output_text(self):
        return self.driver.find_element(*self.EXPECTED_OUTPUT).text

    def editor_is_visible(self):
        return self.driver.find_element(*self.CODE_EDITOR).is_displayed()

    def append_code(self, code):
        """
        Menambahkan kode ke editor (tanpa menghapus kode bawaan)
        """
        editor = self.driver.find_element(*self.CODE_EDITOR)
        editor.click()

        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(code)
        actions.perform()

    def submit_code(self):
        btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def get_result_message(self):
        wait = WebDriverWait(self.driver, 20)

        def result_has_text(driver):
            el = driver.find_element(By.ID, "result")
            return el if el.text.strip() != "" else False

        result_el = wait.until(result_has_text)
        return result_el.text
    
    def close_result_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_BUTTON)
        ).click()

    def get_editor_value(self):
        """
        Ambil isi editor Monaco via JavaScript
        """
        return self.driver.execute_script(
            "return monaco.editor.getModels()[0].getValue();"
        )
    
    def wait_popup_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULT_MESSAGE))

    def is_popup_visible(self):
        try:
            return self.driver.find_element(*self.RESULT_MESSAGE).is_displayed()
        except:
            return False
        
    def click_previous(self):
        element = self.driver.find_element(*self.PREVIOUS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_next(self):
        element = self.driver.find_element(*self.NEXT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    # ===== INFO =====
    def get_current_url(self):
        return self.driver.current_url

    def is_404_page(self):
        return self.ERROR_404_TEXT in self.driver.page_source
    
    def click_other_menu(self):
        self.driver.find_element(*self.OTHER_MENU).click()

    # ===== ALERT HANDLER =====
    def is_confirm_alert_present(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except NoAlertPresentException:
            return None

    # ===== MODAL HANDLER =====
    def is_confirm_modal_visible(self):
        try:
            return self.driver.find_element(*self.CONFIRM_MODAL).is_displayed()
        except:
            return False

    
