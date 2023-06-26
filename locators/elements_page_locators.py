from selenium.webdriver.common.by import By


class TextBoxElementsLocator:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, ".rct-option-expand-all")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, ".rct-option-collapse-all")
    CHECKED_ITEM = (By.CSS_SELECTOR, ".rct-icon-check")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    RESULT_ITEM = (By.CSS_SELECTOR, ".text-success")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
