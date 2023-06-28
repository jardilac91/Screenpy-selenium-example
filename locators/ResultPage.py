from screenpy_selenium import Target
from selenium.webdriver.common.by import By


result = Target.the("result").located_by(
    (By.XPATH, '//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3')
)

result_section = Target.the("result_section").located_by(
    (By.ID, "rso")
)

