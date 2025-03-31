from enum import Enum

class LoginLocator(Enum):
    login_title_locator                 = '//*[@data-gps-track="login.click"]'
    email_title_locator                 = '//label[@for="email"]'
    password_title_locator              = '//label[@for="password"]'

