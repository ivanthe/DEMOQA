import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome('\driver\chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()

