from screenpy_selenium import Target
from selenium.webdriver.common.by import By


URL = "https://github.com"

search_input = Target.the("search_input").located_by(
    (By.NAME, 'q')
)
search_button = Target.the("search_button").located_by(
    (By.NAME, 'btnK')
)