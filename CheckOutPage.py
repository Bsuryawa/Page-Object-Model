from selenium.webdriver.common.by import By



class CheckOutPage:

    phonesList = (By.CLASS_NAME, "card h-100")
    phoneTitle = (By.CLASS_NAME, "card-title")
    buttonTab = (By.CSS_SELECTOR, "button[class*='btn-info']")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutSuccess = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getPhones(self):
        return self.driver.find_elements(*CheckOutPage.phonesList)

    def getPhoneTitle(self):
        return self.driver.find_elements(*CheckOutPage.phoneTitle)
    def button(self):
        return self.driver.find_element(*CheckOutPage.buttonTab)
    def checkOutClick(self):
        return self.driver.find_element(*CheckOutPage.checkOut)
    def checkOutPass(self):
        return self.driver.find_element(*CheckOutPage.checkOutSuccess)