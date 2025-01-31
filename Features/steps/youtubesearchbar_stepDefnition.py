from behave import *
from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
import time

logging.basicConfig(filename="Debug.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@given(u'user launches browser')
def launchBrowser(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    context.driver = webdriver.Chrome(options=chrome_options)
    logging.info("Luanched the browser")
    
@when(u'user opens youtube homepage')
def openYoutube(context):
    context.driver.get("https://www.youtube.com/")
    logging.info("Opened youtube")
    
    
@when(u'user clicks on search bar and enters query "{query}"')
def searchQuery(context,query):
    context.driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/form/input').send_keys(query)
    logging.info("Searched the query in search box")
    time.sleep(2)

@when(u'user clicks the search button with the query')
def search(context):
    context.driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/button').click()
    logging.info("Hit the search button")


@then('user should be redirected to the search results page')
def verify_redirection(context):
    assert "search_query=selenium" in context.driver.current_url, "Did not navigate to the search page"
    time.sleep(5)

@then('user should see videos related to "{query}"')
def verify_search_results(context, query):
    video_titles = context.driver.find_elements(By.XPATH, "//a[@id='video-title']")
    assert any(query.lower() in title.text.lower() for title in video_titles), "No relevant videos found"
    
@then(u'close youtube')
def closeBrowser(context):
    logging.info("youtube closed")
    time.sleep(3)
    context.driver.close()
    