from screenpy_selenium import Target
from selenium.webdriver.common.by import By


results = Target.the("results").located_by(
    (By.CSS_SELECTOR, 'div.codesearch-results > div > div > h3')
)




