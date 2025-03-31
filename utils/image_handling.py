from selenium.webdriver.remote.webelement import WebElement

class ImageHandeling:
    def capture_element_screenshot(element: WebElement):
        return element.screenshot_as_base64