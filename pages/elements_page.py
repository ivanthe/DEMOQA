import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generator_person
from locators.elements_page_locators import TextBoxElementsLocator, CheckBoxLocators, RadioButtonLocators
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

class TextBoxPage(BasePage):
    locator = TextBoxElementsLocator()

    def fill_all_filds(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_address
        permanent_adress = person_info.permanent_address
        self.element_is_present(self.locator.FULL_NAME).send_keys(full_name)
        self.element_is_present(self.locator.EMAIL).send_keys(email)
        self.element_is_present(self.locator.CURRENT_ADDRESS).send_keys(current_adress)
        self.element_is_present(self.locator.PERMANENT_ADDRESS).send_keys(permanent_adress)

        self.element_is_present(self.locator.SUBMIT_BUTTON).click()

        return full_name, email, current_adress, permanent_adress
        # self.element_is_visible(self.*TextBoxElementsLocator.FULL_NAME).send_keys()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locator.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locator.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(self.locator.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_adress = self.element_is_present(self.locator.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress

class CheckBoxPage(BasePage):
    locator = CheckBoxLocators
    def open_full_list(self):
        self.element_is_visible(self.locator.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locator.ITEM_LIST)

        """   ====
        Below is one of the ways to click random list items implemented using a WHILE-loop
        ===   """

        """count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item_list[random.randint(1, 15)])
                item.click()
                count -=1
                #print(item.text)
            else:
                break"""

        random_value = random.randint(1, len(item_list))
        for i in range(0, random_value):
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()

    def get_list_with_clicked_item(self):
        checked_item = self.element_are_present(self.locator.CHECKED_ITEM)
        data = []
        for box in checked_item:
            title_item = box.find_element(By.XPATH, self.locator.TITLE_ITEM)
            data.append(title_item.text.lower().replace(" ", "").split('.')[0])
        return data

    def get_list_with_results(self):
        result_item = self.element_are_present(self.locator.RESULT_ITEM)
        data = []
        for box in result_item:
            data.append(box.text.lower())
        return data

    def compare_results(self, clicked_items, result_item):
        assert clicked_items == result_item, "Результат не совпадает"

class RadioButtonPage(BasePage):
    locators = RadioButtonLocators

    def get_radiobuttons_quantity(self):
        radioButtons_list = self.element_are_present(self.locators.RADIO_BUTTONS_LIST)
        return len(radioButtons_list)

    def click_radio_buttons(self, choise):
        choises = {"yes": self.locators.YES_BUTTON,
                  "impessive": self.locators.IMPRESSIVE_BUTTON,
                  "no": self.locators.NO_BUTTON
                  }
        self.element_is_clickable(choises[choise]).click()

    def get_results(self):
        text = self.element_is_present(self.locators.ACTUAL_RESULT).text
        return text





