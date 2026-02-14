from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    URL = "https://hypermedialearning.sanggadewa.my.id/dashboard"

    # --- USER ICON (pojok kanan atas) ---
    USER_ICON = (
        By.XPATH,
        "//li[contains(@class,'dropdown')]//a[contains(@class,'dropdown-toggle')]"
    )

    # --- MENU DROPDOWN ---
    LOGOUT_MENU = (By.XPATH,"//a[@data-bs-target='#confirmlogout']")

    # --- MODAL ---
    LOGOUT_MODAL = (By.ID, "confirmlogout")
    MODAL_TITLE = (By.ID, "confirmlogoutLabel")

    # --- BUTTON DI MODAL ---
    BUTTON_TIDAK = (
        By.XPATH,
        "//div[@id='confirmlogout']//button[contains(text(),'Tidak')]"
    )

    BUTTON_YA = (
        By.XPATH,
        "//div[@id='confirmlogout']//button[contains(text(),'Ya')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    # =============================
    # ACTIONS
    # =============================

    
    def open_user_dropdown(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.USER_ICON)
        )
        dropdown.click()

        # Tunggu logout menu muncul
        self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_MENU)
        )

    def click_logout_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_MENU)
        ).click()

    def is_logout_modal_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MODAL_TITLE)
        )


    def click_tidak(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_TIDAK)
        ).click()

    def click_ya_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_YA)
        ).click()

    def wait_until_redirect_to_home(self):
        self.wait.until(
            EC.url_to_be("https://hypermedialearning.sanggadewa.my.id/")
        )

