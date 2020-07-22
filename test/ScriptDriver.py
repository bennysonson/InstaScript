"""
Test class for InstaScript
"""

from selenium import webdriver
from time import sleep
from main.Pages import HomePage
from main.Pages import LoginPage
from main.Pages import MainFeed
from main.Pages import AccountFeed

browser = webdriver.Firefox()
browser.implicitly_wait(5)

homePage = HomePage(browser)

loginPage = LoginPage(browser)
""" Insert login info """
loginPage.login("", "")
sleep(3)
mainFeed = MainFeed(browser)
try:
    mainFeed.dontSaveInfo()
except:
    pass
try:
    sleep(2)
    mainFeed.noNotifications()
except:
    pass
sleep(1)
mainFeed = MainFeed(browser)
mainFeed.searchAccount("bennysonson")
sleep(3)
accountFeed = AccountFeed(browser)
accountFeed.likeAllPhotos()
