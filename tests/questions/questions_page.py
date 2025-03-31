import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.change_language import SetLanguage
from utils.definition import settings
from utils.page_processing import PageProcessing
from utils.data_reader import FileLoader
from utils.compare_text import CompareText

from locators.questions.questions_page import LoginLocator

data_path = './data/questions'
languages = FileLoader.load_languages(data_path)

@pytest.fixture(scope="function")
def driver():
    driver = PageProcessing.open_page(settings.SOF_QUESTIONS_PAGE)
    yield driver  
    PageProcessing.close_page(driver)

@pytest.mark.parametrize("language", languages)
def test_login_page(driver : WebDriver, language):
    SetLanguage.set_language(driver,language)

    data_file = FileLoader.load_file_path(data_path,language)
    data = FileLoader.load_json(data_file)
    
    login_title = driver.find_element(By.XPATH, LoginLocator.login_title_locator.value)
    CompareText.compare_text(login_title,data['login']['login'])

    password_title = driver.find_element(By.XPATH, LoginLocator.login_title_locator.value)
    CompareText.compare_text(password_title,"1")



