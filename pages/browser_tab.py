from components.components import WebElement
from pages.base_page import BasePage


class BrowserTab(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/browser-windows"
        super().__init__(driver, self.base_url)
        self.btn_tab = WebElement(driver, "#tabButton")
        self.btn_win = WebElement(driver, "#windowButton")
        self.btn_msg = WebElement(driver, "#messageWindowButton")