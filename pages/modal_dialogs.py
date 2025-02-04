from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)
        self.menu_button = WebElement(driver,"div:nth-child(3) > div > ul > li")
        self.icon = WebElement(driver, '#app > header > a')
        self.showSmallModal = WebElement(driver, '#showSmallModal')
        self.showLargeModal = WebElement(driver, '#showLargeModal')
        self.SmallModal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.LargeModal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.SmallModal_close = WebElement(driver, '#closeSmallModal')
        self.LargeModal_close = WebElement(driver, '#closeLargeModal')
