from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID, "country")
    countryName1 = (By.LINK_TEXT, "India")
    checkbox =(By.CSS_SELECTOR, "div[class*='checkbox']")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def countryName(self):
        self.driver.find_element(*ConfirmPage.country).send_keys("ind")

    def countryNameConfirm(self):

        self.driver.find_element(*ConfirmPage.countryName1).click()

    def  checkboxCompletion(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def submitclick(self):
        self.driver.find_element(*ConfirmPage.submit).click()

    def getSuccessMessage(self):
         return self.driver.find_element(*ConfirmPage.successMessage).text