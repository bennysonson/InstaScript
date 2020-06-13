from time import sleep
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        
    def login(self, username, password):
        usernameInput = self.browser.find_element_by_css_selector("input[name='username']")
        passwordInput = self.browser.find_element_by_css_selector("input[name='password']")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()        
        

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://instagram.com/")

class MainFeed:
    def __init__(self, browser):
        self.browser = browser
        
    def dontSaveInfo(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        
    def noNotifications(self):
        self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        
    def searchAccount(self, text):
        searchBar = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchBar.send_keys(text)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
        
class AccountFeed:
    def __init__(self, browser):
        self.browser = browser
        
    def findPostCount(self):
        return self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").get_attribute('innerHTML')

    def likeFirstPhoto(self):
        try:
            self.browser.find_element_by_xpath("//div[@id='react-root']/section/main/div/div[3]/article/div/div/div/div/a/div/div[2]").click()
        except NoSuchElementException:
            try:
                self.browser.find_element_by_xpath("//div[@id='react-root']/section/main/div/div[2]/article/div/div/div/div/a/div/div[2]").click()
            except NoSuchElementException():
                print("User has no photos or account is private")
        sleep(1)
        #Like first photo
        self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()

    def likePhotos(self, maxPics):
        self.likeFirstPhoto()
        try:
            for _ in range(2, maxPics + 1):
                #Next photo
                self.browser.find_element_by_xpath("//a[contains(text(),'Next')]").click()
                #Like photo
                self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                sleep(2)
        except NoSuchElementException:
            print("Reached end of profile")
        
    def likeAllPhotos(self):
        self.likeFirstPhoto()
        try:
            while (True):
                #Next photo
                self.browser.find_element_by_xpath("//a[contains(text(),'Next')]").click()
                #Like photo
                self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                sleep(2)
        except NoSuchElementException:
            print("End of profile reached")