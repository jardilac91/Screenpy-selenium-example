from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CustomDriver:
    @staticmethod
    def chrome() -> webdriver:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))        