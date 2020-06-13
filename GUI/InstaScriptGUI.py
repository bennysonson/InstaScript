import tkinter as tk
from selenium import webdriver
from time import sleep
from main.Pages import HomePage
from main.Pages import LoginPage
from main.Pages import MainFeed
from main.Pages import AccountFeed
from tkinter import StringVar, OptionMenu



class UserInfo:
    def __init__(self, browser):
        self.browser = browser
        window = tk.Tk()
        self.scriptInfo = tk.Label(text="Enter a valid Instagram username and password").pack()
        tk.Label(text="Usernanme:").pack()
        username = tk.Entry()
        username.pack()
        tk.Label(text="Password:").pack()
        password = tk.Entry()
        password.pack()
        HomePage(browser)
        tk.Button(text="Submit", width=6,height=1, 
                  command=lambda: self.saveAndDestroy(browser, window, username.get(), password.get())).pack()
        window.mainloop()
        
    def saveAndDestroy(self, browser, window, userN, passW):
        LoginPage(self.browser).login(userN, passW)
        sleep(2)
        if (browser.current_url == "https://www.instagram.com/"):
            pass
        window.destroy()
        
class MainAction:
    
    mainOptions = [
        "Like pictures",
        "Option 2",
        "Option 3",
        "Option 4"
        ]
    
    likeOptions = [
        "Like recent photos",
        "Like all photos"
        ]
    
    def __init__(self, browser):
        def submitOption(optionPicked):
            if (optionPicked == self.mainOptions[0]):
                tk.Label(text = "User to perform on").pack()
                userToPerform = tk.Entry()
                userToPerform.pack()
                tk.Button(text = "Submit", width = 6, height = 1,
                          command = lambda: self.likePhotos(userToPerform.get(), mainFeed, browser)).pack()
        self.browser = browser
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
        self.window = tk.Tk()
        tk.Label(text = "Login successful.\nChoose an option").pack()
        variable = StringVar(self.window)
        variable.set(self.mainOptions[0])
        OptionMenu(self.window, variable, *self.mainOptions).pack()
        tk.Button(text = "Submit", width = 6, height = 1, 
                  command = lambda: submitOption(variable.get())).pack()
        self.window.mainloop()

            
    def likePhotos(self, userToPerform, mainFeed, browser):
        mainFeed.searchAccount(userToPerform)
        accountFeed = AccountFeed(browser)
        tk.Label(text = "User has " + accountFeed.findPostCount() + " posts").pack()
        variable = StringVar(self.window)
        variable.set(self.likeOptions[0])
        OptionMenu(self.window, variable, *self.likeOptions).pack()
        tk.Button(text = "Start Liking!", width = 8, height = 1,
                  command = lambda: submitLikeOption(variable.get())).pack()
       
        def submitLikeOption(option):
            if (option == self.likeOptions[0]):
                tk.Label(text = "How many photos to like?").pack()
                numberPhotosToLike = tk.Entry()
                numberPhotosToLike.pack()
                tk.Button(text = "Submit", width = 6, height = 1,
                          command = lambda: accountFeed.likePhotos(int(numberPhotosToLike.get()))).pack()
            elif (option == self.likeOptions[1]):
                accountFeed.likeAllPhotos()
            tk.Label(text = "Done!").pack()
        

def main():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.minimize_window()
    UserInfo(browser)
    MainAction(browser)
    
if __name__ == '__main__':
    main()