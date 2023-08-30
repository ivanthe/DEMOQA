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

class RadioButtonLocators:
    #YES_BUTTON = (By.XPATH, '//input[contains(@id, "yesRadio")]/following-sibling::label')
    #IMPRESSIVE_BUTTON = (By.XPATH, '//input[contains(@id, "impressiveRadio")]/following-sibling::label')
    #NO_BUTTON = (By.XPATH, '//input[contains(@id, "noRadio")]/following-sibling::label')
    ACTUAL_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
    RADIO_BUTTONS_LIST = (By.CSS_SELECTOR, 'input[type="radio"]')
    YES_BUTTON = (By.CSS_SELECTOR, 'label[class^=custom-control-label][for=yesRadio]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, 'label[class^=custom-control-label][for=impressiveRadio]')
    NO_BUTTON = (By.CSS_SELECTOR, 'label[class^=custom-control-label][for=noRadio]')

class WebTableLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')

    REGISTRATION_FORM = (By.CSS_SELECTOR, 'div[class=modal-content]')
    FIRST_NAME_REG_FORM = (By.CSS_SELECTOR, 'input[id=firstName]')
    LAST_NAME_RAG_FORM = (By.CSS_SELECTOR, 'input[id=lastName]')
    EMAIL_REG_FORM = (By.CSS_SELECTOR, 'input[id=userEmail]')
    AGE_REG_FORM = (By.CSS_SELECTOR, 'input[id=age]')
    SALARY_REG_FORM = (By.CSS_SELECTOR, 'input[id=salary]')
    DEPARTMEMT_REG_FORM = (By.CSS_SELECTOR, 'input[id=department]')
    SUBMIT_BUTTON_REG_FORM = (By.CSS_SELECTOR, 'button[id=submit]')

    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div[class=input-group-append]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id=searchBox]')
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title=Edit]')
    UPDATE_BUTTON_BY_ID = (By.CSS_SELECTOR, 'span[id=edit-record-')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title=Delete]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    PEOPLE_DATA = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    X_BUTTON = (By.CSS_SELECTOR, 'span[class=sr-only]')

class ButtonsLocators:
    BUTTON_DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id=doubleClickBtn]')
    BUTTON_RIGHT_CLICK = (By.CSS_SELECTOR, 'button[id=rightClickBtn]')
    BUTTON_LEFT_CLICK = (By.XPATH, '//div[@class="mt-4"][2]/button')

    RESULT_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p[id=doubleClickMessage]')
    RESULT_RIGHT_CLICK = (By.CSS_SELECTOR, 'p[id=rightClickMessage]')
    RESULT_LEFT_CLICK = (By.CSS_SELECTOR, 'p[id=dynamicClickMessage]')


class LinkPageLocators:
    HOME_SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id=simpleLink]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id=bad-request]')





