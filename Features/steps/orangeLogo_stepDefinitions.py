from behave import * 
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="Debug.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
@given(u'launch chrome browsers')
def openBrowser(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    logging.info("WebDriver initialized.")

@when(u'open OrangeHRM homepage')
def openHomepage(context):
    context.driver.get("https://www.orangehrm.com/")
    logging.info("Landing page opened.")


@when(u'verify presence of logo on homepage')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "/html/body/nav/div/a/img")    
    assert logo.is_displayed(), "Logo is not displayed on the homepage"
    logging.info("status verified.")

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()