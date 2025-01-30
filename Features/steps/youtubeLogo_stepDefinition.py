from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import *


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="Debug.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@given(u'launch browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()
    logging.info("launched browser")


@when(u'user is not youtube landing page')
def launchLandingPage(context):
    context.driver.get("https://www.youtube.com/")
    logging.info("opened youtube")

@when(u'presence of logo is verified')
def verifyLogo(context):
    try:
        logo=context.driver.find_element(By.XPATH,'//*[@id="logo-icon"]/span/div')
        if logo.is_displayed():
            logging.info("logo verified")
        else:
            logging.info("No logo")
    except NoSuchElementException:
        logging.info("Element not found")

@then(u'close youtube browser')
def closeBrowser(context):
    logging.info("youtube closed")
    context.driver.close()
