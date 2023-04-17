import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
     homePage = HomePage(self.driver)
     homePage.shopItems()
     #self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
     self.driver.execute_script("window.scrollBy(0,400);")
     #phones = self.driver.find_elements(By.CLASS_NAME, "card h-100")
     checkOutPage = CheckOutPage(self.driver)
     phones = checkOutPage.getPhones()
     for phone in phones:
         #phoneName = phone.find_elements(By.CLASS_NAME,"card-title").text()
         checkOutPage.getPhoneTitle().text()
         if phone == "Blackberry":
             #phone.find_element(By.CSS_SELECTOR, "button[class*='btn-info']").click()
             checkOutPage.buttonClick().click()
             #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click() - click on 'checkout' button
     checkOutPage.checkOutClick().click()
     #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
     checkOutPage.checkOutPass().click()

     #self.driver.find_element(By.ID, "country").send_keys("ind")
     confirm = ConfirmPage(self.driver)
     confirm.countryName()
     wait = WebDriverWait(self.driver, 10)
     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
     #self.driver.find_element(By.LINK_TEXT, "India").click()
     confirm.countryNameConfirm()
     #self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
     confirm.checkboxCompletion()
     #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
     confirm.submitclick()

     #message= self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
     #message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
     message = confirm.getSuccessMessage()
     print(message)
     assert  "Success" in message
             #== "Success! Thank you! Your order will be delivered in next few weeks :-)."

