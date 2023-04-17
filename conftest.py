import pytest as pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope ="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    service_obj = Service(r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(3)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver =driver
    yield
    driver.close()



