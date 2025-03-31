import pytest_check as check
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver

class CompareText:
    @staticmethod
    def compare_text(element : WebElement,expected_result):
        expected_result = str(expected_result)
        check.equal(element.text,expected_result, 
                    "\nExpected text: " + expected_result +
                    "\nActual text: "+ element.text+ 
                    "\n[Screenshot](data:image/png;base64:"+element.screenshot_as_base64)

    @staticmethod
    def compare_text_of_child_text(driver : WebDriver, element : WebElement,expected_result : str,index = 0):
        expected_result = str(expected_result)
        inner_text = driver.execute_script(f"return arguments[0].childNodes[{index}].nodeValue.trim();", element)
        check.equal(inner_text,expected_result, 
                    "\nExpected text: " + expected_result +
                    "\nActual text: "+ element.text+ 
                    "\n[Screenshot](data:image/png;base64:"+element.screenshot_as_base64)

