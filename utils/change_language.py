from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from enum import Enum
class LanguageDisplay(Enum):
    English     = "ENGLISH"
    Japanese    = "日本語"

class SetLanguage:
    @staticmethod
    def set_language(driver : WebDriver, language : str = "English"):
        # try:
        #     language_ele = driver.find_element(By.XPATH, "//span[@class][1]")
        #     current_language = language_ele.text
        #     if current_language != LanguageDisplay[language].value:    
        #         language_ele.click()
        #         expected_language_ele = driver.find_element(By.XPATH,'//div[contains(text(), "'+LanguageDisplay[language].value+'")]')
        #         expected_language_ele.click()
                
        # except Exception as e:
        #     print(e)
        #     raise RuntimeError("Can not change language")
        print("Stack Over Flow doesn't change language")


