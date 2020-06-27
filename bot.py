from selenium import webdriver
import os
import time

class InstaBot:

    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome('./chromedriver.exe')
        self.driver.get("https://www.instagram.com/accounts/login/")


if __name__=='__main__':
    ig_bot=InstaBot('un','pw')
    print(ig_bot.username)