from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
# import time
class PageProcessing:
    @staticmethod
    def open_page(url : str = ""):
        # now = time.time()
        service = Service()
        # print(time.time()-now)

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(5)
        driver.get(url)
        return driver
    
    @staticmethod
    def close_page(driver: WebDriver):
        if driver is not None:  
            driver.quit()